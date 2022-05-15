<template>
  <div class="gallery container-fluid" style="width=60%">
    <b-row class="justify-content-center">
      <b-col>
        <lightbox :images="images" title="Галерея активных меток"></lightbox>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'GalleryView',
  components: {
    
  },
  data () {
    return {
      markers: [],
      images: [],
      errors: [],
    }
  },
  created() {
    axios.get('api/v1/map/markers')
      .then(response => {
        console.log(response.data)
        for (var marker_info of response.data) {
          var image_url = axios.defaults.baseURL + marker_info.image.substring(1);
          this.markers.push({
            'marker_type': marker_info.marker_type,
            'created_on': marker_info.created_on,
            'address': marker_info.address,
            'gps': marker_info.gps,
            'image': image_url,
          });
          this.images.push({
            src: image_url,
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

<style scoped>

</style>