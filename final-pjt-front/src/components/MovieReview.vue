<template>
  <div>
    <MovieReviewItem v-for="(review, key) in reviews" :key="key" :review="review"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieReviewItem from './MovieReviewItem.vue';

export default {
  name: "MovieReview",

  data() {
    return {
      reviews: [],
    };
  },
	props: {
		movieId : Number
	},
  components: {
    MovieReviewItem
  },
  created() {
    const API_URL = this.$store.state.API_URL;
    axios({
      method: "get",
      url: `${API_URL}/api/articles/${this.movieId}/review_movie`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        // console.log(res.data)
        this.reviews = res.data;
      })
      .catch((err) => console.log(err));
  },

  methods: {},
};
</script>

<style lang="scss" scoped></style>
