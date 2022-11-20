<template>
  <div class="MovieDetail">
    <div class="movie-item">
      <div
        class="movie-item__poster"
        :style="`background-image: url(https://image.tmdb.org/t/p/w400/${movie_detail.poster_path})`">
        <!-- <img :src="`https://image.tmdb.org/t/p/w400/${movie.fields.poster_path}`" alt=""> -->
      </div>
      <div class="movie-item__info">
        <h3 class="movie-item__info__title">{{ movie_detail.title }}</h3>
        <div class="movie-item__info__subinfo">
          <span>{{ movie_detail.released_date | getYear }}・</span
          ><span>{{ movie_detail.genres[0]["name"] }}・</span
          ><span>{{ movie_detail.countries[0]["name"] }}</span>
        </div>
      </div>
    </div>
    <!-- 임시로 삽입한 트레일러 영상입니다. -->
    <!-- 임시로 삽입한 배경 이미지입니다.` -->
    <div :style="`background-image: url(https://image.tmdb.org/t/p/w400/${this.backdrop_path})`"></div>
    <!-- 리뷰 생성창으로 이동 -->
    <div class="create-movie-review">
      <button @click="toCreateReview">review create</button>
    </div>
    <!-- 하위컴포넌트인 리뷰를 보여줍니다. -->
    <div class="movie-review">
      <MovieReview :movie_pk="this.movie_pk"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieReview from "@/components/MovieReview.vue";

export default {
  name: "MovieDetail",
  components: {
    MovieReview
  },
  data() {
    return {
      movie_pk: this.$route.params.id,
      movie_detail: {},
      trailer: 'NHA69lCd1ZM', //임시 트레일러 영상 주소
      backdrop_path: '/sPPsR9f4K0movWVQ99u4uMqFzEL.jpg' // 임시 배경
    };
  },

  created() {
    const API_URL = this.$store.state.API_URL;
    axios({
      method: "get",
      url: `${API_URL}/api/movies/${this.movie_pk}/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        // console.log(res.data)
        this.movie_detail = res.data;
        console.log(this.movie_detail);
      })
      .catch((err) => console.log(err));
  },

  methods: {
    toCreateReview() {
      this.$router.push({name: 'reviewCreate', params: {id: this.movie_pk}})
    }
  },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/MovieItem.scss';

.MovieDetail {
    width: calc(100% - 245px);
    height: 100vh;
}
</style>
