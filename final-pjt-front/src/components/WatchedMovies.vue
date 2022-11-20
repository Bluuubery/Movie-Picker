<template>
  <div>
    <h1>WatchedMovies</h1>
		<hr>
		<!-- WatchedMovie에 속해있는 개별 영화들을 보여주는 컴포넌트입니다. -->
    <WatchedMoviesItem
      v-for="(watchedMovie, key) in watchedMovies"
      :key="key"
      :watchedMovie="watchedMovie"
    />
  </div>
</template>

<script>
import axios from "axios";
import WatchedMoviesItem from "./WatchedMoviesItem.vue";

export default {
  name: "WatchedMovies",
  components: {
    WatchedMoviesItem,
  },
  props: {
    user_pk: Number,
  },
  data() {
    return {
      watchedMovies: [],
    };
  },
  created() {
		// user_pk를 인자로 보내 해당 유저의 WatchedMovies를 받아오는 axios 요청입니다. 
    const API_URL = this.$store.state.API_URL;
    axios({
      method: "get",
      url: `${API_URL}/api/accounts/${this.user_pk}/watched/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        // console.log(res.data)
        this.watchedMovies = res.data.watched_movies;
      })
      .catch((err) => console.log(err));
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
