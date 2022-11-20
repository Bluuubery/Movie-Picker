<template>
  <div>
    <!-- 임시로 영화 제목과 포스터를 렌더링합니다. -->
    <h1>title: {{ toWatchMovie.title }}</h1>
    <div
      class="movie-item__poster"
      :style="`width: 300px; height: 400px; background-image: url(https://image.tmdb.org/t/p/w400/${this.toWatchMovie.poster_path})`"
    ></div>
  </div>
</template>

<script>
export default {
  name: "ToWatchMoviesItem",
  props: {
    // 개별 영화의 정보를 객체 형태로 받아옵니다.
    toWatchMovie: Object,
  },
  data() {
    return {};
  },

  mounted() {},

  methods: {
    // 해당 영화의 디테일 페이지로 보내주는 메서드입니다. 이후 프론트 작업 시 템플릿이랑 연결해주세요
    toDetail() {
      this.$router.push({name: 'movieDetail', params: {movieId: this.movie.id}})
    }
  },
};
</script>

<style lang="scss" scoped></style>
