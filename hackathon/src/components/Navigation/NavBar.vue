<template>
  <b-navbar variant="faded" id="b-navbar-my">
    <b-navbar-brand>
      <b-row>
        <!-- <img id="navbar-brand-img" src="https://placekitten.com/g/30/30" height="50.39158630371094px" width="55.094974517822266px" class="d-inline-block align-top" alt="Kitten" :to="{name: 'map'}"> -->
        <a href="/"><img id="navbar-brand-img" :src="logoSVG"></a>
      </b-row>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item class="my-nav-item" :to="{name: 'map'}" exact>Карта</b-nav-item>
        <b-nav-item class="my-nav-item" :to="{name: 'gallery'}">Галерея</b-nav-item>
        <b-nav-item class="my-nav-item" :to="{name: 'archive'}">Архив</b-nav-item>
        <b-nav-item class="my-nav-item" :to="{name: 'about'}">О Нас</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  components: {
    
  },
  data() {
    return {
      logoSVG: require('@/assets/GorDorogiLogo.svg')
    }
  }
}
</script>

<style scoped>
.my-nav-item {
  margin-right: 2em;
  color: #000000;
}

.router-link-active {
  background-color: #05FF00;
  color: #000000;
  border-radius: 0.2em;
}

#b-navbar-my {
  background-color: #FFFFFF;
}

#nav-link-text {
  font-family: Inter;
  font-size: 20px;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  color: #000000;
}

#navbar-brand-img {
  margin-left: 1em;
}

#navbar-brand-title {
  margin-left: 0.5em;
  margin-top: 0.2em;
  color: #000000;
  background-color: none !important;
}

#header-1 {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: #000000;
}

#header-2 {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}
</style>