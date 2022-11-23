<template>
  <div class="home">
    <SearchBar/>
    <div class="home__main-container" >
      <div class="alert" v-if="!this.best_movie">
          <h2 class="alert__heading">인생영화가 아직 없습니다.</h2>
          <router-link to="/game" class="gameLink-alert">
            <h2>인생영화 찾으러 가기</h2>
            <svg width="96" height="110" viewBox="0 0 96 110" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M93.9857 59.8555C96.6643 57.1699 96.6643 52.8086 93.9857 50.123L59.7 15.748C57.0214 13.0625 52.6714 13.0625 49.9929 15.748C47.3143 18.4336 47.3143 22.7949 49.9929 25.4805L72.6 48.125H6.85714C3.06429 48.125 0 51.1973 0 55C0 58.8027 3.06429 61.875 6.85714 61.875H72.5786L50.0143 84.5195C47.3357 87.2051 47.3357 91.5664 50.0143 94.252C52.6929 96.9375 57.0429 96.9375 59.7214 94.252L94.0071 59.877L93.9857 59.8555Z" fill="url(#paint0_radial_252_146)"/>
              <defs>
              <radialGradient id="paint0_radial_252_146" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(28.1661 38.6912) rotate(42.55) scale(103.776 103.619)">
              <stop stop-color="#FFB3F3"/>
              <stop offset="1" stop-color="#BA63FF"/>
              </radialGradient>
              </defs>
            </svg>
          </router-link>
      </div>

      <div class="header" ref="header">
        <div class="best-movie" v-if="this.best_movie">
          <h2 class="best-movie__heading">
            내 인생영화
          </h2>
          <div class="best-movie__main-info">
            <div class="best-movie__main-info__poster"
            v-if="this.best_movie"
            @click="goMovieDetail(best_movie.movie.id)"
            :style="`background-image: url(https://image.tmdb.org/t/p/w400/${this.best_movie.movie.poster_path})`">
            </div>
            <div class="best-movie__main-info__content">
              <h2 class="best-movie__main-info__content__date">{{this.best_movie.created_at | formatDate }}</h2>
              <h3 class="best-movie__main-info__content__title">{{ this.best_movie.movie.title }}</h3>
              <div class="best-movie__main-info__content__subinfo">
                <span>{{ this.best_movie.movie.released_date | formatYear }}・</span
                ><span>{{ this.best_movie.movie.genres[0]["name"] }}・</span
                ><span>{{ this.best_movie.movie.countries[0]["name"] }}</span>
              </div>
              <p>{{ this.best_movie.movie.overview}}</p>
            </div>
          </div>
        </div>
        
        <router-link to="/game" class="gameLink" v-if="this.best_movie">
          <h2>인생영화 월드컵</h2>
          <svg width="96" height="110" viewBox="0 0 96 110" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M93.9857 59.8555C96.6643 57.1699 96.6643 52.8086 93.9857 50.123L59.7 15.748C57.0214 13.0625 52.6714 13.0625 49.9929 15.748C47.3143 18.4336 47.3143 22.7949 49.9929 25.4805L72.6 48.125H6.85714C3.06429 48.125 0 51.1973 0 55C0 58.8027 3.06429 61.875 6.85714 61.875H72.5786L50.0143 84.5195C47.3357 87.2051 47.3357 91.5664 50.0143 94.252C52.6929 96.9375 57.0429 96.9375 59.7214 94.252L94.0071 59.877L93.9857 59.8555Z" fill="url(#paint0_radial_252_146)"/>
            <defs>
            <radialGradient id="paint0_radial_252_146" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(28.1661 38.6912) rotate(42.55) scale(103.776 103.619)">
            <stop stop-color="#FFB3F3"/>
            <stop offset="1" stop-color="#BA63FF"/>
            </radialGradient>
            </defs>
          </svg>
        </router-link>
      </div>
      <div class="content-wrapper" v-if="this.best_movie">
        <div class="recommends">
          <h2 class="recommends__title">오늘의 추천영화</h2>
          <div class="recommends__list">
            <MovieItem v-for="(movie, key) in this.myRecommendations" :key="key" :movie="movie"/>
          </div>
        </div>
        <div class="records">
          <h2 class="records__title">내 인생영화 기록</h2>
          <div class="records__list"
          v-if="this.best_Movie_records.length">
            <MyRecordItem
            v-for="(feedItem, key) in this.best_Movie_records.slice().reverse()"
            :key="key"
            :feedItem="feedItem"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar';
import MovieItem from '@/components/MovieItem.vue';
import MyRecordItem from '@/components/MyRecordItem';
// import _ from 'lodash';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    SearchBar,
    MovieItem,
    MyRecordItem,
  },
  data() {
    return {
      watched_movies: this.$store.state.watched_movies,
      myRecommendations: [],
    }
  },
  // 컴포넌트 가드
  beforeCreate() {
    this.$store.dispatch('getUser')
  },
  created() {
    this.getMyRecommendations()
  },
  mounted() {
    this.setHeader()
    this.clearSearchBar();
  },
  methods: {
    clearSearchBar() {
      const searchInput = document.querySelector('.search-bar__form input[type="text"]')
      searchInput.value = null;
    },
    // 영화 디테일 페이지로 이동
    goMovieDetail(movieId) {
      this.$router.push({ name: 'movieDetail', params: { movieId: movieId }})
    },
    // 인생영화 월드컵 페이지로 이동
    goGame(event) {
      const gameName = event.target.dataset.gamename
      this.$router.push({ name: 'game', params: { gameName: gameName } })
    },

    // 내 추천 영화(랜덤)을 API GET 요청
    getMyRecommendations() {
      const API_URL = this.$store.state.API_URL;
      axios({
        method: "GET",
        url: `${API_URL}/api/accounts/get_my_recommendations/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.myRecommendations = res.data;
        })
        .catch((err) => console.log('recommendations', err));
    },

    // header 배경 이미지 설정
    setHeader() {
      if (this.best_movie) {
        const header = this.$refs.header
        header.style.backgroundImage = `linear-gradient(to bottom, rgba(20, 18, 23, 1), rgba(20, 18, 23, 0.8)), url(https://image.tmdb.org/t/p/original/${this.best_movie.movie.backdrop_path})`
      } else {
        const home = document.querySelector('.home')
        home.style.backgroundImage = `linear-gradient(to bottom, rgba(20, 18, 23, 1), rgba(20, 18, 23, 0.8)), url(https://www.themoviedb.org/t/p/original/nyuzfjAbuSel6dVKY4zFo95ugUf.jpg)`
      }
    }
  },
  computed: {
    // 인생영화
    best_movie() {
      return this.$store.state.best_movie
    },

    // 명예의 전당 리스트
    best_Movie_records() {
      let best_movies = this.$store.state.all_best_movies
      best_movies = best_movies.filter((best_movie) => best_movie.movie.id !== this.best_movie.movie.id)
      return best_movies
    },
    // 인생영화 월드컵 배경 사진 고르기
    // allMoviePosterPath() {
    //   return `https://image.tmdb.org/t/p/w400/${_.sample(this.$store.state.watched_movies).poster_path}`
    // },

    
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