<template>
  <div>
		{{movieDetail.title}}
	</div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RecommendedMoviesItem",
	props: {
		movieId: Number
	},

  data() {
    return {
			movieDetail: {}
		};
  },
	created() {
    const API_URL = this.$store.state.API_URL;
    axios({
      method: "get",
      url: `${API_URL}/api/movies/${this.movieId}/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        // console.log(res.data)
        this.movieDetail = res.data;
      })
      .catch((err) => console.log(err));
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
