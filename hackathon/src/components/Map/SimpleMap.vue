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
        <l-marker v-for="(marker, index) in markers" :key="index" ref="myMarker" :lat-lng="marker.latLng">
            <l-icon
            v-if="marker.marker_type == 0"
            :icon-size="staticIconSize"
            :icon-anchor="staticAnchor"
            icon-url="https://www.pngall.com/wp-content/uploads/2017/05/Map-Marker-PNG-File.png"
            >
            </l-icon>
            <l-icon
            v-else
            :icon-size="staticIconSize"
            :icon-anchor="staticAnchor"
            icon-url="https://www.pngall.com/wp-content/uploads/2017/05/Map-Marker-PNG-Image.png"
            >
            </l-icon>
            <l-popup>
                <div @click="innerClick">
                    <!-- <img src="{{ marker.thumbnail }}" alt="..." /> -->
                    {{ marker.name }}
                    <p v-show="showParagraph">
                        {{ marker.description }}
                    </p>
                </div>
            </l-popup>
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
            staticIconSize: [32, 37],
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