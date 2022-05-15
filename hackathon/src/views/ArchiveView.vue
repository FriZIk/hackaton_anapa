<template>
  <div class="gallery container-fluid">
    <!-- <b-card-group class="col-md-3" v-for="marker in markers">
          <b-card class="archive-card" :img-src="marker.image" img-alt="Card image" img-right img-width="300px" img-height="auto">
            <b-card-text>
              <p class="card-text">{{ marker.gps }}</p>
              <p class="card-text">{{ marker.address }}</p>
              <p class="card-text">{{ marker.created_on }}</p>
            </b-card-text>
          </b-card>
        </b-card-group> -->
    
    <h1 class="text-center" style="margin-bottom: 0.3em;">Архив меток</h1>
    <div class="container-fluid d-flex h-100 justify-content-center align-items-center p-0">
    <b-row class="row-cols-1 row-cols-md-2" style="width: 80%">
      <b-col class="col-mb-6 " v-for="marker in markers">
        <b-card class="archive-card" :img-src="marker.image" img-alt="Card image" img-right>
          <b-card-text id="card-text">
            <p id="card-address" class="card-text text-left">{{ marker.address }}</p>
            <br>
            <p id="card-created-on" class="card-text text-left"><span class="font-weight-bold">Дата: </span>{{ marker.created_on }}</p>
            <br>
            <p id="card-gps" class="card-text text-left"><span class="font-weight-bold">Координаты: </span>{{ marker.gps }}</p>
            <br>
            <p id="card-tag" class="card-text text-left"><span class="font-weight-bold">Тег: </span>{{ marker.marker_type }}</p>
            <br>
            <p id="card-cause" class="card-text text-left"><span class="font-weight-bold">//Типо устранено по такой-то причине//</span></p>
            <br>
          </b-card-text>
        </b-card>
      </b-col>

    </b-row>
    </div>
  </div>
</template>

<style scoped>
@media screen and (max-width: 600px) {
  .archive-card img {
    display: none !important;
  }
}

#card-text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 24px;
  margin-left: 2em;
  margin-top: 1em;
  word-wrap: break-word;
  overflow-wrap: anywhere
}

.archive-card {
  margin-bottom: 1.5em;
  max-width:100%;
}

#card-address {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 21px;
  line-height: 30px;
}

.archive-card img {
  margin: 2em;
  border-radius: 0.15em;
  width: auto;
  max-width: 200px;
  height: 250px;
  object-fit: cover;
  margin-top: auto;
  margin-bottom: auto;
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'ArchiveView',
  components: {
    
  },
  data () {
    return {
      markers: [],
      errors: [],
    }
  },
  created() {
    axios.get('api/v1/map/markers')
      .then(response => {
        console.log(response.data)
        for (var marker_info of response.data) {
          var image_url = axios.defaults.baseURL + marker_info.image.substring(1);
          const options = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };
          var created_on = new Date(marker_info.created_on).toLocaleDateString('ru-ru', options);
          console.log(created_on);
          var marker_type = "Повреждения на дороге"
          if (marker_info.marker_type === 1) {
            marker_type = "Проблема со знаком"
          } else if (marker_info.marker_type === 2) {
            marker_type = "Проблема с разметкой"
          }
          this.markers.push({
            'marker_type': marker_type,
            'created_on': created_on,
            'address': marker_info.address,
            'gps': marker_info.gps,
            'image': image_url,
          });
        }
        console.log(this.markers)
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e)
      })
  }
}
</script>