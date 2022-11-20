<template>
  <div>
    <h1>RecommendedMovies</h1>
		<!-- ToWatchMovies에 속해있는 개별 영화들을 보여주는 컴포넌트입니다. -->
    <RecommendedMoviesItem v-for="(movieId, key) in this.recommendedMoviesTemp" :key="key" :movie-id="movieId"/>
		<!-- db 연동 후 해당 코드로 대체해주세요 -->
    <!-- <RecommendedMoviesItem v-for="(movieId, key) in this.recommendedMovies" :key="key" :movie-id="movieId"/> -->
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
			// 임시로 설정한 추천영화 목록입니다.(이후 movie_detail로부터 받아옴)
			recommendedMoviesTemp: [38, 120467, 49047, 152532, 194662, 106646, 264660, 210577, 11324, 44214, 77, 37165, 76203, 244786, 141, 194, 694, 19913, 14, 641, 242582]
		};
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
