<template>
  <b-navbar variant="faded" id="b-navbar-my">
    <b-navbar-brand>
      <b-row>
        <img id="navbar-brand-img" src="https://placekitten.com/g/30/30" height="50.39158630371094px" width="55.094974517822266px" class="d-inline-block align-top" alt="Kitten">
        <router-link id="navbar-brand-title" to="/">
          <p id="header-1" style="line-height: 10px;">Городские</p>
          <p id="header-2" style="line-height: 10px;">Дороги</p>
        </router-link>
      </b-row>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav id="navbar-nav-my" class="ml-auto">
        <b-nav-item class="nav-item-my">
          <router-link to="/">
            <p id="nav-link-text" class="text-center">
              Карта
            </p>
          </router-link>
        </b-nav-item>

        <b-nav-item class="nav-item-my">
          <router-link to="/archive/">
            <p id="nav-link-text" class="text-center">
               Архив
            </p>
          </router-link>
        </b-nav-item>

        <b-nav-item class="nav-item-my">
          <router-link to="/gallery/">
            <p id="nav-link-text" class="text-center">
              Галерея
            </p>
          </router-link>
        </b-nav-item>

        <b-nav-item class="nav-item-my">
          <router-link to="/about/">
            <p id="nav-link-text" class="text-center">
              О Нас
            </p>
          </router-link>
        </b-nav-item>
      </b-navbar-nav>      
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  components: {
    
  },
}
</script>

<style scoped>
#navbar-nav-my {
  margin-top: 0.7em;
}

#b-navbar-my {
  background-color: #222222;
}

#nav-link-text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  margin-right: 2em;
  color: #ffffff;
}

#navbar-brand-img {
  margin-left: 1em;
}

#navbar-brand-title {
  margin-left: 0.5em;
  margin-top: 0.2em;
  color: #ffffff;
  background-color: none !important;
}

#header-1 {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: #ffffff;
}

#header-2 {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #ffffff;
}
</style>