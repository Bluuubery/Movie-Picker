<template>
  <div>
    <!-- 임시로 영화 제목과 포스터를 렌더링합니다. -->
    <h1>title: {{ watchedMovie.title }}</h1>
    <div
      class="movie-item__poster"
      :style="`width: 300px; height: 400px; background-image: url(https://image.tmdb.org/t/p/w400/${this.watchedMovie.poster_path})`"
    ></div>
  </div>
</template>

<script>
export default {
  name: "WatchedMoviesItem",
  props: {
    watchedMovie: Object,
  },
  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style lang="scss" scoped></style>
