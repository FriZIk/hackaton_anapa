import Vue from 'vue'
import VueRouter from 'vue-router'

import MapView from '@/views/MapView.vue'
import ArchiveView from '@/views/ArchiveView.vue'
import GalleryView from '@/views/GalleryView.vue'
import AboutView from '@/views/AboutView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'map',
    component: MapView
  },
  {
    path: '/archive/',
    name: 'archive',
    component: ArchiveView
  },
  {
    path: '/gallery/',
    name: 'gallery',
    component: GalleryView
  },
  {
    path: '/about/',
    name: 'about',
    component: AboutView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
