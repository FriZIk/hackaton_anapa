<template>
  <div class="map container-fluid">
    <b-row style="margin-left: 1%; margin-right: 1%; margin-top: 2%; margin-bottom: 1%;">
      <b-col class="col-lg-4 col-md-4 col-sm-3 col-xs-3" id="card-col">
        <b-card
          no-body
          img-src=""
          img-alt="Image"
          img-top
          style="min-height: 80vh;"
          id="card"
        >
          <b-card-body id="card-body">
            <b-card-title id="card-title" ref="card-title-ref" class="text-left font-weight-bold">{{card_title_text}}</b-card-title>
            <img id="card-image" :src='card_image_url !== null ? card_image_url : null'>
            <b-card-text id="card-text" class="text-left" v-html="card_body_text">
            </b-card-text>
            <b-button class="float-left" id="button-delete-marker" v-if='is_marker_selected===true' v-b-modal.modal-prevent-closing>Удалить метку</b-button>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col class="col-lg-8 col-md-8 col-sm-7 col-xs-9" style="min-height: 80vh;">
        <b-container id="simple-map" style="width: 100%; height: 100%;">
          <SimpleMap @clickonmarker="clickOnMarker" />
        </b-container>
      </b-col>
    </b-row>
    <b-row>
      <div class="col-12"><span id="footer-text-1" class="float-left">Сделано командой CRAFSED</span> <span id="footer-text-2" class="float-right">Copyright &copy; {{ current_year }}, городские дороги</span></div>
    </b-row>

    <div>
      <b-modal
        id="modal-prevent-closing"
        ref="modal"
        title="Удаление метки"
        @show="resetModal"
        @hidden="resetModal"
        @ok="handleOk"
      >
        <form ref="form" @submit.stop.prevent="handleSubmit">
          <!-- <b-form-group label="Причина удаления" v-slot="{ deletionReason }">
            <b-form-radio-group
              id="delete-form-btn-radios"
              invalid-feedback="Необходимо выбрать причину удаления"
              v-model="form_radio_delete_selected"
              :options="form_radio_delete_options"
              :aria-describedby="deletionReason"
              button-variant="outline-success"
              name="radio-btn-stacked"
              buttons
              stacked
            ></b-form-radio-group>
          </b-form-group> -->
          <b-form-radio-group v-model="form_radio_delete_selected" :options="form_radio_delete_options" :state="state" name="radio-validation">
            <b-form-invalid-feedback :state="state">Выберите причину удаления</b-form-invalid-feedback>
            <b-form-valid-feedback :state="state">Спасибо</b-form-valid-feedback>
          </b-form-radio-group>
        </form>

        <template #modal-footer="{ ok, cancel }">
          <b-button size="sm" variant="danger" @click="cancel()">
            Cancel
          </b-button>
          <b-button size="sm" variant="success" @click="ok()">
            OK
          </b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
import SimpleMap from '@/components/Map/SimpleMap.vue'
import axios from 'axios'

export default {
  name: 'MapView',
  components: {
    SimpleMap,
  },
  data() {
    return {
      selected_marker: {},
      is_marker_selected: null,
      card_title_text: 'Как пользоваться сервисом?',
      card_body_text: `С помощью этого сервиса вы можете контролировать состояние объектов городской инфраструктуры.
      <br><br>Нажмите на метку, чтобы увидеть фото, дату и координаты дефекта, распознаного нейронной сетью. Метку можно удалить.
      <br><br>В разделе “Архив” вы можете изучить динамику составления и удаления меток. В “Галерее” хранятся фото всех распознанных дефектов.<br>`,
      card_image_url: null,
      current_year: new Date().getFullYear(),
      form_radio_delete_options: [
        { text: 'Ошибка фиксации', value: 'radio1' },
        { text: 'Дефект устранён', value: 'radio2' },
      ],
      form_radio_delete_selected: null,
    }
  },
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity()
      this.nameState = valid
      return valid
    },
    resetModal() {
      this.form_radio_delete_selected = ''
    },
    handleOk(bvModalEvent) {
      // Prevent modal from closing
      bvModalEvent.preventDefault()
      // Trigger submit handler
      this.handleSubmit()
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return
      }
      // Push the name to submitted names
      // this.submittedNames.push(this.name)
      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide('modal-prevent-closing')
      })
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    clickOnMarker(marker) {
      var marker_type = "Повреждения на дороге"
      if (marker.marker_type === 1) {
        marker_type = "Проблема со знаком"
      } else if (marker.marker_type === 2) {
        marker_type = "Проблема с разметкой"
      }
      var gps = marker.latLng.lat + ',' + marker.latLng.lng;
      const options = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };
      var created_on = new Date(marker.created_on).toLocaleDateString('ru-ru', options);
      var image_url = axios.defaults.baseURL + marker.image.substring(1);
      // marker.address;
      this.selected_marker = {
        "marker_type": marker_type,
        "address": marker.address,
        "gps": gps,
        "created_on": created_on,
        "image_url": image_url,
      }
      // change data in map CARD
      this.is_marker_selected = true;
      this.card_title_text = this.capitalizeFirstLetter(marker.address);
      this.card_image_url = image_url;
      this.card_body_text = `
      <p class="card-text text-left"><span class="font-weight-bold">Дата: </span>${created_on}</p>
      <br>
      <p class="card-text text-left"><span class="font-weight-bold">Координаты: </span>${gps}</p>
      <br>
      <p class="card-text text-left"><span class="font-weight-bold">Тег: </span>${marker_type}</p>
      
      `
    },
  },
  computed: {
    state() {
      return Boolean(this.form_radio_delete_selected)
    }
  },
}
</script>

<style scoped>
@media screen and (max-width: 1024px) {
  #card-col {
    display: none !important;
  }
}

#button-delete-marker {
  background-color: #05FF00;
  color: #000000;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
}

#footer-text-1 {
  font-family: 'Inter';
  font-style: italic;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;

  padding-bottom: 0;
  padding-left: 0;
  margin-bottom: 0;
  margin-left: 3em;
}

#footer-text-2 {
  font-family: 'Inter';
  font-style: italic;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;

  padding-bottom: 0;
  padding-right: 0;
  margin-bottom: 0;
  margin-right: 3em;
}

#card {
  filter: drop-shadow(0px 4px 25px rgba(0, 0, 0, 0.25));
}

#card-title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 45px;
  line-height: 54px;
  color: #000000;
}

#card-text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}

#card-body {
  margin: 30px;
}

#simple-map {
  filter: drop-shadow(0px 4px 20px rgba(0, 0, 0, 0.25));
}

#card-image {
  position: inline-block;
  width: 100%;
  height: auto;
  margin-top: 0.3em;
  margin-bottom: 1em;
  border-radius: 0.2em;
}
</style>