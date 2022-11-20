<template>
  <!-- <div class="page-wrapper">

  </div> -->
  <div class="home">
    <div class="home__search-container">
      <SearchBar/>
    </div>
    <div class="home__main-container">
      <div class="home__main-container__left">
        <div class="best-movie">
          <h1 class="home-title">내 인생영화</h1>
          <div class="container" @click="goMovieDetail(best_movie.movie.id)">
            <div class="best-movie__poster">
              <!-- add poster here -->
              <img :src="bestMovie_imgSrc" alt="">
            </div>
            <div class="best-movie__info">
              <h4 class="best-movie__info__date">
                {{ best_movie.created_at | formatDate }}
              </h4>
              <h3 class="best-movie__info__movie-title">
                {{ best_movie.movie.title }}
              </h3>
              <div class="best-movie__info__movie-info">
                <span>{{ best_movie.movie.released_date | formatYear }}・</span><span>{{ best_movie.movie.genres[0]["name"] }}・</span><span>{{ best_movie.movie.countries[0]["name"] }}</span>
              </div>
              <div class="best-movie__info__comment">
                <h4>내 코멘트</h4>
                <div class="best-movie__info__comment__content">
                  대상(Her)이 주체(She)가 되는 순간에 찾아오는 어른의 사랑.
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="world-cup">
          <h1 class="home-title">내 인생영화 찾기</h1>
          <div class="container">
            <div class="world-cup__game" @click="goGame($event)" data-gameName="all-movie">모든 영화</div>
            <div class="world-cup__game">코미디 영화</div>
            <div class="world-cup__game">액션 영화</div>
            <div class="world-cup__game">미국 영화</div>
            <div class="world-cup__game">한국 영화</div>
            <div class="world-cup__game">직접 설정</div>
          </div>
        </div>
      </div>
      <div class="home__main-container__right">
        <h1 class="home-title">명예의 전당</h1>
        <div class="container">
          <div class="record" v-for="record in best_Movie_records" :key="record.id">
            <div class="record__poster">
              <img :src="`https://image.tmdb.org/t/p/w200/${record.movie.poster_path}`" alt="">
            </div>
            <div class="record__info">
              <h3 class="record__info__date">{{ record.created_at | formatDate }}</h3>
              <h2 class="record__info__title">{{ record.movie.title}}</h2>
              <div class="record__info__movie-info">
                <span>{{ best_movie.movie.released_date | formatYear }}・</span><span>{{ best_movie.movie.genres[0]["name"] }}・</span><span>{{ best_movie.movie.countries[0]["name"] }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
// import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    SearchBar,
  },
  data() {
    return {
      watched_movies: this.$store.state.watched_movies
    }
  },
  created() {
    this.$store.dispatch('getUser')
  },
  mounted() {
    this.clearSearchBar();
  },
  methods: {
    // getUser() {
    //   if (this.isLogin) {
    //     this.$store.dispatch('getUser');
    //   } else {
    //     // this.$router.push({ name: 'login'})
    //   }
    // },
    clearSearchBar() {
      const searchInput = document.querySelector('.search-bar__form input[type="text"]')
      // console.log(searchInput)
      searchInput.value = null;
    },
    // 영화 디테일 페이지로 이동
    goMovieDetail(movieId) {
      // console.log(movieId)
      this.$router.push({ name: 'movieDetail', params: { movieId: movieId }})
    },
    // 인생영화 월드컵 페이지로 이동
    goGame(event) {
      const gameName = event.target.dataset.gamename
      this.$router.push({ name: 'game', params: { gameName: gameName } })
    }
  },
  computed: {
    // 인생영화
    best_movie() {
      return this.$store.state.best_movie
    },
    // 명예의 전당 리스트
    // best_movies() {
    //   return this.$store.state.all_best_movies
    // },
    // 인생영화 포스터 이미지 url
    bestMovie_imgSrc() {
      const IMG_SIZE = 'w200';
      const poster_path = this.best_movie.movie.poster_path;
      const img_url = `https://image.tmdb.org/t/p/${IMG_SIZE}/${poster_path}`
      return img_url
    },
    // 명예의 전당 리스트
    best_Movie_records() {
      return this.$store.state.all_best_movies
    },
  },
  filters: {
    formatDate(date) {
      const y = date.slice(0, 4)
      const m = date.slice(5, 7)
      const d = date.slice(8, 10)
      const result = `${y}.${m}.${d}`
      return result
    },
    formatYear(date) {
      const y = date.slice(0, 4)
      return y
    }
  }
}
</script>

<style lang="scss">
@import '../assets/scss/HomeView.scss';


</style>