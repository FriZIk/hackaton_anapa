import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import '@/assets/app.scss'

Vue.config.productionTip = false

import { Icon } from 'leaflet'
import { LMap, LTileLayer, LMarker, LPopup, LTooltip, LIcon, LControlZoom } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component('l-popup', LPopup)
Vue.component('l-tooltip', LTooltip)
Vue.component('l-icon', LIcon)
Vue.component('l-control-zoom', LControlZoom)

delete Icon.Default.prototype._getIconUrl
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
})

import axios from 'axios';

axios.defaults.baseURL = 'http://api.gordorogi.tk/';

import lightbox from 'vlightbox'

Vue.use(lightbox)

new Vue({
  router,
  axios,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
