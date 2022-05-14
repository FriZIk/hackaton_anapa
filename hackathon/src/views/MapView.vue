<template>
  <div class="map container-fluid">
    <b-row class="justify-content-center" style="margin-left: 1%; margin-right: 1%; margin-top: 2%; margin-bottom: 1%;">
      <b-col class="col-xs-6 col-md-4">
        <b-card
          no-body
          img-alt="Image"
          img-top
          style="min-height: 80vh;"
          id="card"
        >
          <b-card-body id="card-body">
            <b-card-title id="card-title" class="text-left font-weight-bold">Как пользоваться сервисом?</b-card-title>
            <br>
            <b-card-text id="card-text" class="text-left">
              С помощью этого сервиса вы можете контролировать состояние объектов городской инфраструктуры.
              <br><br>
              Нажмите на метку, чтобы увидеть фото, дату и координаты дефекта, распознаного нейронной сетью. Метку можно удалить.
              <br><br>
              В разделе “Архив” вы можете изучить динамику составления и удаления меток. В “Галерее” хранятся фото всех распознанных дефектов.
              <br>
            </b-card-text>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col class="col-xs-12 col-sm-6 col-md-8">
        <b-container id="simple-map" style="width: 100%; height: 100%;">
          <SimpleMap />
        </b-container>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import SimpleMap from '@/components/Map/SimpleMap.vue'
export default {
  name: 'MapView',
  components: {
    SimpleMap,
  },
}
</script>

<style scoped>
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
</style>