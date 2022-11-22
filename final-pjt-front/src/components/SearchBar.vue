<template>
  <div class="search-bar">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc.<path d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352c79.5 0 144-64.5 144-144s-64.5-144-144-144S64 128.5 64 208s64.5 144 144 144z"/></svg>
    <form action="" class="search-bar__form">
      <input type="text" placeholder="영화 바로 검색하기" @focus="goSearch" @input="searchMovie($event)">
      <input type="submit" value="">
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchBar',

  data() {
    return {
      results: null,
    };
  },

  mounted() {
    
  },

  methods: {
    // search로 이동
    goSearch() {
      if (this.$route.name !== 'search') {
        this.$router.push({ name: 'search'})
      }
    },
    // index로 돌아가기
    goBackHome() {
      this.$router.push({ name: 'home'})
    },
    // input 이벤트 핸들러 : 영화 검색 api 요청
    searchMovie(event) {
      const query = event.target.value
      const API_URL = this.$store.state.API_URL
      const SEARCH_URL = `${API_URL}/api/movies/search_movie/${query}/`
      axios({
        method: 'get',
        url: SEARCH_URL,
        headers: {
            // Authorization: `Token 6023611848bfca271b0de4cb5db50064289b791d` //임시 토큰
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then(res => {
        const movies = res.data
        this.results = movies
        console.log(this.results)
      })
      .then(() => {
        this.$emit('getResults', this.results)
      })
    },
    // 유저를 검색하는 axios 요청입니다.(메서드만 작성, 이후 프론트 작업 시 필요한 컴포넌트에 등록해주세요)
    searchUser() {}
  },
};
</script>

<style lang="scss">
@import '@/assets/scss/SearchBar.scss';
</style>