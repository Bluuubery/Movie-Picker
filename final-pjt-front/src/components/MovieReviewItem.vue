<template>
  <div>
    <h1>title: {{ review.title }}</h1>
    <h1>username: {{ review.username }}</h1>
    <h1>content: {{ review.content }}</h1>
    <!-- <h1>{{review.movie}}</h1> -->
  </div>
</template>

<script>
export default {
  name: "MovieReviewItem",
  props: {
    review: Object,
  },

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style lang="scss" scoped></style>
