<template>
  <div class="form-container">
      <h2 class="form-container__title">로그인</h2>
      <form action="" class="form-container__form" @submit.prevent="signUp">
        <div class="form-container__form__input">
          <label for="username">아이디</label>
          <input type="text" id="username" placeholder="아이디" v-model="username">
        </div>
        <div class="form-container__form__input">
          <label for="password">비밀번호</label>
          <input type="password" id="password" placeholder="비밀번호" v-model="password1">
        </div>
        <div class="form-container__form__input">
          <label for="password">비밀번호 확인</label>
          <input type="password" id="password" placeholder="비밀번호 확인" v-model="password2">
        </div>
        <input type="button" value="회원가입" class="form-container__form__submit">
      </form>
      <div>
        <span class="form-container__comment">이미 회원이 아니신가요?</span>
        <router-link to="/login" class="form-container__link">로그인</router-link>
      </div>
    </div>
</template>

<script>
export default {
  name: 'SignupForm',

  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },

  methods: {
    signUp() {
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        email, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    }
  },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/LoginView.scss';
</style>