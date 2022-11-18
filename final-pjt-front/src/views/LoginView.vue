<template>
  <div class="login-view">
    <div class="wrapper">
      <div class="wrapper__logo">
        무비피커
      </div>
      <LoginForm/>
    </div>
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue'

export default {
  name: 'LoginView',
  components: {
    LoginForm,
  },

  data() {
    return {
      
    };
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/LoginView.scss';
</style>