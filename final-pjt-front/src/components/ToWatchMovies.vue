<template>
  <div>
    <h1>ToWatchMovies</h1>
    <hr />
    <!-- ToWatchMovies에 속해있는 개별 영화들을 보여주는 컴포넌트입니다. -->
    <ToWatchMoviesItem
      v-for="(toWatchMovie, key) in toWatchMovies"
      :key="key"
      :toWatchMovie="toWatchMovie"
    />
  </div>
</template>

<script>
import axios from "axios";
import ToWatchMoviesItem from "./ToWatchMoviesItem.vue";

export default {
  name: "ToWatchMovies",
  components: {
    ToWatchMoviesItem,
  },
  props: {
    user_pk: String,
  },
  data() {
    return {
      toWatchMovies: [],
    };
  },
  created() {
    // user_pk를 인자로 보내 해당 유저의 ToWatchMovie를 받아오는 axios 요청입니다.
    const API_URL = this.$store.state.API_URL;
    axios({
      method: "get",
      url: `${API_URL}/api/accounts/${this.user_pk}/to_watch/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        // console.log(res.data)
        this.toWatchMovies = res.data.to_watch_movies;
      })
      .catch((err) => console.log(err));
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
