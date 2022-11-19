<template>
  <div class="movie-item" @click="clickMovie($event), toDetail(), $emit('addMovie')" :data-moviePK="movie.id">
    <div class="movie-item__poster" :style="`background-image: url(https://image.tmdb.org/t/p/w400/${movie.poster_path})`">
      <!-- <img :src="`https://image.tmdb.org/t/p/w400/${movie.fields.poster_path}`" alt=""> -->
    </div>
    <div class="movie-item__info">
      <h3 class="movie-item__info__title">{{ movie.title }}</h3>
      <div class="movie-item__info__subinfo">
        <span>{{ movie.released_date | getYear }}・</span><span>{{ movie.genres[0]["name"] }}・</span><span>{{ movie.countries[0]["name"] }}</span>
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
    // 한 영화 클릭 > clicked 클래스 추가
    clickMovie(event) {
      // console.log('clicked!')
      const target = event.currentTarget.children[0];
      target.classList.toggle('clicked');
      return
    },
    toDetail() {
      this.$router.push({name: 'movieDetail', params: {id: this.movie.id}})
    }
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