<template>
    <l-map
    v-if="showMap"
    :zoom="zoom"
    :center="center"
    :options="mapOptions"
    style="height: 100%"
    @update:center="centerUpdate"
    @update:zoom="zoomUpdate"
    >
        <l-tile-layer :url="url" :attribution="attribution" />
        <l-marker @click='$emit("clickonmarker", marker)' v-for="(marker, index) in markers" :key="index" ref="myMarker" :lat-lng="marker.latLng">
            <l-icon
            v-if="marker.marker_type === 0"
            :icon-size="staticIconSize"
            :icon-anchor="staticAnchor"
            icon-url="https://i.imgur.com/sHfnquh.png"
            >
            </l-icon>
            <l-icon
            v-else-if="marker.marker_type === 1"
            :icon-size="staticIconSize"
            :icon-anchor="staticAnchor"
            icon-url="https://i.imgur.com/pXwZTrF.png"
            >
            </l-icon>
            <l-icon
            v-else
            :icon-size="staticIconSize"
            :icon-anchor="staticAnchor"
            icon-url="https://i.imgur.com/VuZ6mwp.png"
            >
            </l-icon>
        </l-marker>
    <l-control-zoom position="bottomright"  ></l-control-zoom>
    </l-map>
</template>

<script>
import { latLng, icon } from 'leaflet'
import axios from 'axios'
export default {
    name: 'SimpleMap',
    data() {
        return {
            zoom: 14,
            center: latLng(44.8870225,37.327779),
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution: '<a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            // withPopup: latLng(47.41322, -1.219482),
            // withTooltip: latLng(47.41422, -1.250482),
            markers: [],
            currentZoom: 11.5,
            currentCenter: latLng(44.8870225,37.327779),
            showParagraph: true,
            mapOptions: {
                zoomSnap: 0.5,
                attributionControl: false,
                zoomControl: false,
            },
            showMap: true,
            staticAnchor: [16, 37],
            staticIconSize: [32, 50],
            errors: []
        };
    },
    created() {
        axios.get('api/v1/map/markers')
            .then(response => {
                console.log(response.data)
                for (var marker_info of response.data) {
                    var coords = marker_info.gps.split(',')
                    this.markers.push(
                        {
                            'marker_type': marker_info.marker_type,
                            'created_on': marker_info.created_on,
                            'address': marker_info.address,
                            'latLng': latLng(coords[0], coords[1]),
                            'image': marker_info.image,
                        }
                    )
                }
                console.log(this.markers)
            })
            .catch(e => {
                this.errors.push(e)
                console.log(e)
            })
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        showLongText() {
            this.showParagraph = !this.showParagraph;
        },
        innerClick() {
            alert("Click!")
        },
        aboba() {
            console.log('aboba clicked');
        }
    },
    computed: {
        dynamicSize() {
            return [this.iconSize, this.iconSize]
        },
        dynamicAnchor() {
            return [this.iconSize / 2, this.iconSize]
        },
    }
}
</script>

<style scoped>
</style>