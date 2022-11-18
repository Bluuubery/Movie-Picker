<template>
    <div class="form-container">
      <h2 class="form-container__title">로그인</h2>
      <form action="" class="form-container__form" @submit.prevent="login">
        <div class="form-container__form__input">
          <label for="username">아이디</label>
          <input type="text" id="username" placeholder="아이디" v-model="username">
        </div>
        <div class="form-container__form__input">
          <label for="password">비밀번호</label>
          <input type="password" id="password" placeholder="비밀번호" v-model="password">
        </div>
        <input type="submit" value="로그인" class="form-container__form__submit">
      </form>
      <div>
        <span class="form-container__comment">아직 회원이 아니신가요?</span>
        <router-link to="/signup" class="form-container__link">회원가입</router-link>
      </div>
    </div>
</template>

<script>
export default {
  name: 'LoginForm',

  data() {
    return {
      username: null,
      password: null,
    };
  },

  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    }
  },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/LoginView.scss';
</style>