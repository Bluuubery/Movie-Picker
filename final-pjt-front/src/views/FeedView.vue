<template>
  <div class="FeedView">
    <UserSearchBar/>
    <div class="wrapper">
      <!-- 자식 컴포넌트에게 각각의 피드 아이템을 내려줍니다. -->
      <FeedItem v-for="(feedItem, key) in feed" :key="key" :feed-item="feedItem"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import FeedItem from '@/components/FeedItem';
import UserSearchBar from '@/components/UserSearchBar';

export default {
  name: 'FeedView',

  components: {
    FeedItem,
    UserSearchBar,
  },

  data() {
    return{
      // 피드에 속한 게시글이 array형태로 들어있습니다.(각각의 피드는 object)
      feed: [],
    }
  },
  // 요청 보낸 유저(자신)의 피드에 대한 GET API요청을 보냅니다.
  created() {
    const API_URL = this.$store.state.API_URL;
    axios({
      method: "get",
      url: `${API_URL}/api/accounts/feed/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        this.feed = res.data;
      })
      .catch((err) => console.log(err));
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/FeedView.scss';
</style>