<template>
  <div>
    <h1>ReviewCreate</h1>
    <form @submit.prevent="reviewCreate">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /><br />
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea
      ><br />
      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "ReviewCreateView",

  data() {
    return {
			movieId: this.$route.params.movieId,
			title: null,
			content: null
		};
  },
  methods: {
		reviewCreate() {
      const content = this.content;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }

			const API_URL = this.$store.state.API_URL;
      console.log(API_URL)

      axios({
        method: "POST",
        url: `${API_URL}/api/articles/${this.movieId}/review_create/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        data: {
          content,
        },
      })
        .then(() => {
					this.$router.push({name: 'movieDetail', params: {movieId: this.movieId}})
        })
        .catch((err) => {
          console.log(err);
        });
    },
	},
};
</script>

<style lang="scss" scoped></style>
