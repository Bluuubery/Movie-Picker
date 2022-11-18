<template>
  <div class="movie-item" @click="movieDetail">
    <div class="movie-item__poster" :style="`background-image: url(https://image.tmdb.org/t/p/w400/${movie.fields.poster_path})`">
      <!-- <img :src="`https://image.tmdb.org/t/p/w400/${movie.fields.poster_path}`" alt=""> -->
    </div>
    <div class="movie-item__info">
      <h3 class="movie-item__info__title">{{ movie.fields.title }}</h3>
      <div class="movie-item__info__subinfo">
        <span>{{ movie.fields.released_date | getYear }}・</span><span>country</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: Object,
  },

  data() {
    return {
      
    };
  },

  mounted() {
    
  },

  methods: {
    movieDetail() {
      return
    },
  },
  filters: {
    getYear(date) {
      const y = date.slice(0, 4)
      return y
    }
  }
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/MovieItem.scss'
</style>