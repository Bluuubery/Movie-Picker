<template>
  <div id="app" class="app">
    <nav class="navbar" v-if="!['login', 'signup', 'first-addMovie', 'game', 'NotFound404'].includes($route.name)">
      <router-link to="/">
        <div class="navbar__logo">무비피커</div>
      </router-link>  
      <router-link :to="{ name: 'userDetail', params: { userId: this.$store.state.user_pk }}" class="navbar__user">
        <!-- 프로필 이미지 임시로 추가(스타일링 필요) -->
        <div class="navbar__user-profile" :style="`background-image: url(${this.$store.state.API_URL}${this.$store.state.avatar}); background-size: cover; width:50px; height: 50px;`">

        </div>
        <h3>{{ this.$store.state.username}}</h3>
      </router-link>
      <div class="navbar__routers">
        <router-link to="/" :class="{ 'active' : $route.name === 'home' }">
          <img v-if="this.$route.name === 'home'" src="./assets/img/nav_icon_grad03.svg" alt="">
          <img v-else src="./assets/img/nav_icon_white03.svg" alt="">
          <h3 :class="{ 'active' : $route.name === 'home' }">대시보드</h3>
        </router-link>
        <router-link to="/addMovie" :class="{ 'active' : $route.name === 'addMovie' }">
          <img v-if="this.$route.name === 'addMovie'" src="./assets/img/nav_icon_grad02.svg" alt="">
          <img v-else src="./assets/img/nav_icon_white02.svg" alt="">
          
          <h3 :class="{ 'active' : $route.name === 'addMovie' }">랜덤영화 찾기</h3>
        </router-link>
        <router-link :to="{name: 'feed', params: {userId: this.$store.state.user_pk}}" :class="{ 'active' : $route.name === 'feed' }">
          <img v-if="this.$route.name === 'feed'" src="./assets/img/nav_icon_grad01.svg" alt="">
          <img v-else src="./assets/img/nav_icon_white01.svg" alt="">
          
          <h3 :class="{ 'active' : $route.name === 'feed' }">내 피드</h3>
        </router-link>
      </div>
      <div class="navbar__logout-container">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M534.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-128-128c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L434.7 224 224 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l210.7 0-73.4 73.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l128-128zM192 96c17.7 0 32-14.3 32-32s-14.3-32-32-32l-64 0c-53 0-96 43-96 96l0 256c0 53 43 96 96 96l64 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-64 0c-17.7 0-32-14.3-32-32l0-256c0-17.7 14.3-32 32-32l64 0z"/></svg>
          <h2 class="logout-container__title" @click="logout">로그아웃</h2>
      </div>
    </nav>
    <div class="app__container">
      <div class="app__container__search-container"  v-if="!['login', 'signup', 'first-addMovie', 'userDetail', 'addMovie'].includes($route.name)">
        <SearchBar/>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'

export default {
  components: {
    SearchBar,
  },
  methods: {
    logout(){
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/scss/reset.scss';
@import '@/assets/scss/common.scss';
@import '@/assets/scss/main.scss';
@import '@/assets/scss/navbar.scss';
</style>
