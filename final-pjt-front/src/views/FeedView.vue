<template>
  <div>
    <h1>FeedView</h1>
    <hr />
    <!-- 보고 싶은 영화 컴포넌트입니다. 유저 피케이로 접근해서 해당 유저의 보고 싶은 영화를 보여줍니다. -->
    <ToWatchMovies :user_pk="this.user_pk" />
    <hr />
    <!-- 본 영화 컴포넌트입니다. 유저 피케이로 접근해서 해당 유저의 본 영화를 보여줍니다. -->
    <WatchedMovies :user_pk="this.user_pk" />
  </div>
</template>

<script>
import ToWatchMovies from "@/components/ToWatchMovies.vue";
import WatchedMovies from "@/components/WatchedMovies.vue";

export default {
  name: "FeedView",
  components: {
    ToWatchMovies,
    WatchedMovies,
  },
  data() {
    return {
      user_pk: this.$route.params.userId,
    };
  },
  mounted() {},
  methods: {},
};
</script>

<style lang="scss" scoped></style>
