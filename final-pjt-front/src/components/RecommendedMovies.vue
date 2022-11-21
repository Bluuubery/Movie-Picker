<template>
  <div>
    <h1>RecommendedMovies</h1>
		<!-- ToWatchMovies에 속해있는 개별 영화들을 보여주는 컴포넌트입니다. -->
    <RecommendedMoviesItem v-for="(movieId, key) in this.recommendedMovies" :key="key" :movie-id="movieId"/>
  </div>
</template>

<script>
import RecommendedMoviesItem from "./RecommendedMoviesItem.vue";

export default {
  name: "RecommendedMovies",
  props: {
		// 상위 view인 MovieDetail로부터 추천영화의 정보를 어레이 형태로 받아옵니다. 
    recommendedMovies: Array,
  },
  components: {
    RecommendedMoviesItem,
  },
  data() {
    return {
				};
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
