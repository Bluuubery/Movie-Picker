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
			movie_pk: this.$route.params.movie_pk,
			title: null,
			content: null
		};
  },
  methods: {
		reviewCreate() {
      const title = this.title;
      const content = this.content;
      if (!title) {
        alert("제목을 입력해주세요");
        return;
      } else if (!content) {
        alert("내용을 입력해주세요");
        return;
      }

			const API_URL = this.$store.state.API_URL;

      axios({
        method: "post",
        url: `${API_URL}/api/articles/${this.movie_pk}/review_create/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        data: {
          title,
          content,
        },
      })
        .then(() => {
					this.$router.push({name: 'movieDetail', params: {id: this.movie_pk}})
        })
        .catch((err) => {
          console.log(err);
        });
    },
	},
};
</script>

<style lang="scss" scoped></style>
