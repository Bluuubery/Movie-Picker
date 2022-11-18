<template>
    <div class="wrapper">
        <div class="greeting">
            <h2 class="greeting__line1">안녕하세요, <span><strong>username</strong></span>! </h2>
            <h2 class="greeting__line2">본 영화를 선택해주세요 </h2>
        </div>
        <div class="movie-container">
            <div class="movie-container__btns">
                <button>목록 새로고침</button>
            </div>
            <div class="movie-container__list">
                <MovieItem v-for="(movie, key) in movies.slice(0, 20)" :key="key" :movie="movie"/>
            </div>
        </div>
    </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue';
// import axios from 'axios';
import movies from '@/../../src/assets/movie_data.json';

export default {
    name: 'FirstAddMovieView',
    components: {
        MovieItem
    },

    data() {
        return {
            movies: null,
        };
    },

    // greeting 나오는 동안 로딩되게 할 수 있을까?
    created() {
        this.getMovies();
    },

    methods: {
        getMovies() {
            // const API_URL = 'http://127.0.0.1:8000/api/movies';
            // axios({
            //     method: 'get',
            //     url: `${API_URL}/`,
            //     headers: {
            //         Authorization: `Token ${ this.$store.state.token }`
            //     }
            // })
            // .then(res => {
            //     const movies = res.data;
            //     this.movies = movies;
            // })

            // 임시 데이터 가져오기
            this.movies = movies;
        }
    },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/FirstAddMovieView.scss';
</style>