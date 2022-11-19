<template>
    <div class="wrapper">
        <div class="greeting">
            <h2 class="greeting__line1">안녕하세요, <span><strong>{{ this.$store.state.username }}</strong></span>! </h2>
            <h2 class="greeting__line2">본 영화를 선택해주세요 </h2>
        </div>
        <div class="movie-container">
            <div class="movie-container__btns">
                <button @click="refreshMovieList">목록 새로고침</button>
                <button @click="postUserMovies">선택 완료</button>
            </div>
            <div class="movie-container__list">
                <MovieItem v-on:addMovie="addMovie" v-for="(movie, key) in movies" :key="key" :movie="movie"/>
            </div>
        </div>
    </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue';
// import axios from 'axios';
// import movies from './@/../../assets/movie_data.json';
import axios from 'axios';
// import Vue from 'vue';

// Vue.forceUpdate();

export default {
    name: 'FirstAddMovieView',
    components: {
        MovieItem
    },

    data() {
        return {
            all_movies: [],
            movies: [],
            clickedMoviesPk: [],
            // page: 1,
        };
    },
    watch: {
        movies: {
        },
        // movies: {
        //     // computed 속성 v-model로 쓰려면 setters가 필요
        //     get: function() {
        //         return this.all_movies.slice(20 * this.page - 20, 20 * this.page)
        //     },
        //     set: function(newMovies) {
        //         return this.newMovies.slice(20 * this.page - 20, 20 * this.page)
        //     }
        // }
        // // function() {
        // //     return this.all_movies.slice(20 * this.page - 20, 20 * this.page);
        // // }
    },

    created() {
        this.getMovies();
        this.clickedMoviesPk = [];
    },

    methods: {
        // 영화 데이터 20개씩 가져오기
        getMovies() {
            const API_URL = this.$store.state.API_URL;
            axios({
                method: 'get',
                url: `${API_URL}/api/movies/movie_list_small/`,
                headers: {
                    // Authorization: `Token 6023611848bfca271b0de4cb5db50064289b791d` //임시 토큰
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then(res => {
                console.log(res.data)
                this.movies = res.data;
            })
            // .catch(err => console.log('err', err))

            // 임시 데이터 가져오기
            // this.movies = movies;
        },

        // 클릭한 영화 data에 추가
        addMovie() {
            const clickedMovies = document.querySelectorAll('.clicked');
            let clickedMoviesPk = [];
            clickedMovies.forEach((movie) => {
                clickedMoviesPk.push(movie.parentNode.dataset.moviepk)});
            this.clickedMoviesPk = clickedMoviesPk;
            return
        },

        // 영화 목록 새로고침
        refreshMovieList() {
            this.getMovies();
            const clickedMovies = document.querySelectorAll('.clicked');
            clickedMovies.forEach((movie) => movie.classList.remove('clicked'));
        },
        
        // 유저의 watched_movie POST 요청 보내기
        postUserMovies() {
            const API_URL = this.$store.state.API_URL;
            const user_pk = this.$store.state.user_pk; 
            this.clickedMoviesPk.forEach((movie_pk) => {
                axios({
                    method: 'post',
                    url: `${API_URL}/api/accounts/${user_pk}/${movie_pk}/watched/`,
                    headers: {
                    // Authorization: `Token 6023611848bfca271b0de4cb5db50064289b791d` //임시 토큰
                    Authorization: `Token ${ this.$store.state.token }`
                    }
                })
                .then(() => {
                    this.refreshWatchedMovies()
                    this.$router.push({ name: 'home' })
                })
                .catch(err => console.log(err))
            })
        },

        // watchedmovies를 state에 반영해주는 메서드
        refreshWatchedMovies(){
            const API_URL = this.$store.state.API_URL;
            const user_pk = this.$store.state.user_pk; 
            axios({
                method: 'GET',
                url: `${API_URL}/api/accounts/${user_pk}/watched/`,
                headers: {
                Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res) => {
                this.$store.commit('REFRESH_WATCHED_MOVIES', res.data)
            })
        }
    },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/FirstAddMovieView.scss';
</style>