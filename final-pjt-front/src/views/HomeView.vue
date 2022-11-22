<template>
  <!-- <div class="page-wrapper">

  </div> -->
  <div class="home">
    <!-- <div class="home__search-container"> -->
      <SearchBar/>
    <!-- </div> -->
    <div class="home__main-container">
      <div class="home__main-container__left">
        <div class="best-movie">
          <h1 class="home-title">내 인생영화</h1>
          <div class="container" @click="goMovieDetail(best_movie.movie.id)">
            <div class="best-movie__poster" v-if="best_movie">
              <!-- add poster here -->
              <img :src="bestMovie_imgSrc" alt="">
            </div>
            <div class="best-movie__info" v-if="best_movie">
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
            <div class="best-movie__none" v-else>
              <h2>{{ this.$store.state.username }}의 인생영화가 아직 없습니다.</h2>
              <h2> '내 인생영화 찾기'를 진행해주세요.</h2>
            </div>
          </div>
        </div>
        <div class="world-cup">
          <h1 class="home-title">인생영화 월드컵</h1>
          <div class="container">
            <div class="world-cup__game" @click="goGame($event)" data-gameName="all-movie"
            :style="`background-image: url(${allMoviePosterPath})`"
            >모든 영화</div>
            <div class="world-cup__game"
            v-if="genreComedyPosterPath"
            :style="`background-image: url(https://image.tmdb.org/t/p/w400/${genreComedyPosterPath})`"
            >코미디 영화</div>
            <div class="world-cup__game"
            v-if="genreActionPosterPath"
            :style="`background-image: url(https://image.tmdb.org/t/p/w400/${genreActionPosterPath})`"
            >액션 영화</div>
            <div class="world-cup__game">미국 영화</div>
            <div class="world-cup__game">한국 영화</div>
            <div class="world-cup__game">직접 설정</div>
          </div>
        </div>
      </div>
      <div class="home__main-container__right">
        <h1 class="home-title">인생영화 기록</h1>
        <div class="container">
          <div v-if="!best_movie">
            <h2>{{ this.$store.state.username }}의 인생영화가 아직 없습니다.</h2>
              <h2> '내 인생영화 찾기'를 진행해주세요.</h2>
          </div>
          <div class="record" v-for="(record, key) in best_Movie_records" :key="-key" @click="goMovieDetail(record.movie.id)">
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
import SearchBar from '@/components/SearchBar';
import _ from 'lodash';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    SearchBar,
  },
  data() {
    return {
      watched_movies: this.$store.state.watched_movies,
      // 유저가 선택한 인생영화에 기반해서 임의의 추천영화 20개를 제공합니다(유저가 선택한 인생 영화가 적으면 그보다 적을 수 있음)
      myRecommendations: []
      // 아래는 데이터가 제공되는 예시입니다. 프론트 작업 시 참고 후 삭제해주세요
      // [
      //   {
      //       "id": 425,
      //       "genres": [
      //           {
      //               "id": 12,
      //               "name": "모험"
      //           },
      //           {
      //               "id": 16,
      //               "name": "애니메이션"
      //           },
      //           {
      //               "id": 35,
      //               "name": "코미디"
      //           },
      //           {
      //               "id": 10751,
      //               "name": "가족"
      //           }
      //       ],
      //       "countries": [
      //           {
      //               "id": 2,
      //               "name": "미국"
      //           }
      //       ],
      //       "title": "아이스 에이지",
      //       "original_title": "Ice Age",
      //       "released_date": "2002-03-10",
      //       "popularity": 201.563,
      //       "vote_count": 11515,
      //       "vote_avg": 7.3,
      //       "overview": "거대한 빙하가 온 지구의 표면을 뒤덮기 시작하던 때, 모든 동물들은 따뜻한 남쪽나라로 이동을 시작하지만, 염세적인 털북숭이 맘모스 만프레드만은 유별나게 북쪽으로 향한다. 만프레드는 우연히 떠버리 나무늘보 시드를 만나고, 인간의 아이 로샨을 발견한 뒤 가족을 찾아주기로 한다. 이들은 여행길에 검치 호랑이 디에고와 동행하게 되지만, 디에고는 비밀스런 임무를 맡고 있는 처지다. 바로 호랑이 무리의 두목으로부터 끼니를 때울 만한 인간의 아이를 납치해오라는 명령을 받은 것이다. 과연 로샨은 무사히 가족의 품으로 돌아갈 수 있을까?",
      //       "poster_path": "/biwqSbuyxjrZMvVcb8Lsv3GyQbw.jpg",
      //       "backdrop_path": "/a9ykRAWtQnI3SsZDfh8sCJo5cWI.jpg",
      //       "trailer_path": "CZShn0PZiYU",
      //       "recommended": [
      //           12,
      //           585,
      //           808,
      //           809,
      //           810,
      //           812,
      //           862,
      //           863,
      //           920,
      //           950,
      //           953,
      //           2062,
      //           8355,
      //           8587,
      //           9502,
      //           9806,
      //           10527,
      //           20352,
      //           38757,
      //           57800,
      //           278154
      //       ]
      //   },
      //   ...
      // ]
    }
  },
  created() {
    this.$store.dispatch('getUser')
  },
  mounted() {
    this.clearSearchBar();
    this.getMyRecommendations()
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
    },

    // 내 추천 영화(랜덤)을 API GET 요청으로 불러오는 메서드입니다.(mounted에 실행됩니다.)
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
          // console.log(res.data)
          this.myRecommendations = res.data;
        })
        .catch((err) => console.log(err));
    }
  },
  computed: {
    // 인생영화
    best_movie() {
      return this.$store.state.best_movie
    },

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
    // 인생영화 월드컵 배경 사진 고르기
    allMoviePosterPath() {
      return `https://image.tmdb.org/t/p/w400/${_.sample(this.$store.state.watched_movies).poster_path}`
    },

    // 장르별 인생영화 월드컵 포스터
    genreComedyPosterPath() {
      const movies = this.$store.state.watched_movies.filter((movie) => Object.values(Object.values(movie.genres)).includes("코미디"))
      if (movies.length) {
        return _.sample(movies).poster_path
      } else {
        return null;
      }
    },
    genreActionPosterPath() {
      const movies = this.$store.state.watched_movies.filter((movie) => {
        const genresObj = Object.values(Object.values(movie.genres))
        console.log(Object.entries(genresObj))
        // Object.values(Object.values(movie.genres)).filter((genre) => genre.name )
        Object.values(Object.values(movie.genres)).includes("액션")
      })
      if (movies.length) {
        return _.sample(movies).poster_path
      } else {
        return null;
      }
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