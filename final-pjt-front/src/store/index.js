import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000';

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    // auth
    token: null,
    username: null,
    user_pk: 1, // 임시 유저 번호

    // 인생영화
    best_movie: {
      "id": 1,
      "movie": {
          "id": 12,
          "title": "니모를 찾아서",
          "released_date": "2003-05-30",
          "popularity": 133.931,
          "vote_count": 16988,
          "vote_avg": 7.8,
          "overview": "광대어 말린은 아내 코랄과 2세들의 부화를 기다리던 중 상어의 습격을 받는다. 알을 보호하려던 아내는 행방불명되고, 유일하게 살아남은 아기에게 말린은 니모라는 이름을 붙인다. 사건 이후 큰 바다를 무조건 겁내게 된 말린은 니모를 과보호한다. 하지만 니모는 등교 첫날 잠수부에게 납치돼 시드니에 있는 치과의사의 수족관에 끌려가고, 슬픔으로 혼비백산한 아빠 말린은 평소의 심약함을 잊고니모를 찾아나선다. 단기기억상실증을 지닌 명랑한 물고기 도리의 도움으로 상어, 심해어, 해파리의 위협을 뚫고 동호주 해류로 향하는 동안, 니모는 수족관의 새 친구들과 탈출을 모의한다.",
          "poster_path": "/9ViCYfZ0whpwtKbM2WJP5PfsG2x.jpg",
          "genres": [
              "애니메이션"
          ]
      },
      "created_at": "2022-11-16T14:52:44.511746",
      "best_of_best": false,
      "user": [
          1
      ]
    },
    // 모든 인생영화 기록들
    all_best_movies: [
      {
        "id": 1,
        "movie": {
            "id": 12,
            "title": "니모를 찾아서",
            "released_date": "2003-05-30",
            "popularity": 133.931,
            "vote_count": 16988,
            "vote_avg": 7.8,
            "overview": "광대어 말린은 아내 코랄과 2세들의 부화를 기다리던 중 상어의 습격을 받는다. 알을 보호하려던 아내는 행방불명되고, 유일하게 살아남은 아기에게 말린은 니모라는 이름을 붙인다. 사건 이후 큰 바다를 무조건 겁내게 된 말린은 니모를 과보호한다. 하지만 니모는 등교 첫날 잠수부에게 납치돼 시드니에 있는 치과의사의 수족관에 끌려가고, 슬픔으로 혼비백산한 아빠 말린은 평소의 심약함을 잊고니모를 찾아나선다. 단기기억상실증을 지닌 명랑한 물고기 도리의 도움으로 상어, 심해어, 해파리의 위협을 뚫고 동호주 해류로 향하는 동안, 니모는 수족관의 새 친구들과 탈출을 모의한다.",
            "poster_path": "/9ViCYfZ0whpwtKbM2WJP5PfsG2x.jpg",
            "genres": [
                12
            ]
        },
        "created_at": "2022-11-16T14:52:44.511746",
        "best_of_best": false,
        "user": [
            1
        ]
      },
      {
          "id": 3,
          "movie": {
              "id": 95,
              "title": "아마겟돈",
              "released_date": "1998-07-01",
              "popularity": 70.354,
              "vote_count": 6853,
              "vote_avg": 6.8,
              "overview": "미국 동부에 운석이 떨어진다. 이는 뉴욕 크기의 소행성이 지구를 향해 돌진하고 있는 증거임을 미국 우주 항공국이 밝힌다. 텍사스 크기의 소행성이 시속 2만 3천 마일의 속도로 지구로 돌진한다는 사실을 알게 되자 나사(미국 항공 우주국)는 대책을 세운다. 남은 시간은 18일. 지구를 구할 유일한 방법은 돌진하는 소행성에 구멍을 뚫어 핵폭탄을 장착, 궤도를 바꾸는 것이다.  지구 최고의 유정 굴착 기술자들이 파견된다. 해리(브루스 윌리스)는 굴착 기술의 전문가로 지구를 구하기 위해 짧은 시간 동안 우주 비행에 대한 교육을 받고 그의 동료들과 소행성으로 떠난다. 프리덤호와 인디펜던스호는 소행성에 접근하지만 인디펜던스호는 유성의 파편을 맞고 추락한다.  해리 일행은 어쩔 수 없이 도착한 인원으로 폭탄 장치를 하기 위해 최선을 다하지만 무선 폭파 장치가 고장나 누군가 그곳에 남아야 하는데...  임무를 무사히 마친 후 지구로 돌아가서 해리의 딸인 그레이스(리브 타일러)와 결혼하기로 한 A.J(벤 애플렉)는 해리와 지구를 구하기 위해 자신이 소행성에 남기로 하나 결정적인 순간 해리는 딸을 위해서 자신이 소행성에 남는데...",
              "poster_path": "/8T9xKzzSZij7dxy3ybkingQvoIZ.jpg",
              "genres": [
                  12,
                  28,
                  53,
                  878
              ]
          },
          "created_at": "2022-11-16T15:48:47.485650",
          "best_of_best": false,
          "user": [
              1
          ]
      },
      {
          "id": 3,
          "movie": {
              "title": "블랙 팬서: 와칸다 포에버",
              "released_date": "2022-11-09",
              "popularity": 4853.507,
              "vote_count": 533,
              "vote_avg": 7.6,
              "overview": "국왕이자 블랙 팬서인 티찰라의 죽음 이후 수많은 강대국으로부터 위협을 받게 된 와칸다. 라몬다, 슈리 그리고 나키아, 오코예, 음바쿠는 각자 사명감을 갖고 와칸다를 지키기 위해 외로운 싸움을 이어간다. 한편, 비브라늄의 패권을 둘러싼 미스터리한 음모와 함께 깊은 해저에서 모습을 드러낸 최강의 적 네이머와 탈로칸의 전사들은 와칸다를 향해 무차별 공격을 퍼붓기 시작하는데…",
              "poster_path": "/3PCRWLeqp5y20k6XVzcamZR3BWF.jpg",
              "genres": [
                28,
                12,
                878
              ]
          },
          "created_at": "2022-11-16T15:48:47.485650",
          "best_of_best": false,
          "user": [
              1
          ]
      },
      {
          "id": 3,
          "movie": {
            "title": "탑건: 매버릭",
            "released_date": "2022-05-24",
            "popularity": 1180.077,
            "vote_count": 4736,
            "vote_avg": 8.3,
            "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데...",
            "poster_path": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
            "genres": [
              28,
              18
            ]
          },
          "created_at": "2022-11-16T15:48:47.485650",
          "best_of_best": false,
          "user": [
              1
          ]
      },
      {
          "id": 3,
          "movie": {
            "title": "토르: 러브 앤 썬더",
            "released_date": "2022-07-06",
            "popularity": 1192.811,
            "vote_count": 4637,
            "vote_avg": 6.7,
            "overview": "이너피스를 위해 자아 찾기 여정을 떠난 천둥의 신 토르. 그러나 우주의 모든 신들을 몰살하려는 신 도살자 고르의 등장으로 토르의 안식년 계획은 산산조각 나 버린다. 토르는새로운 위협에 맞서기 위해 킹 발키리, 코르그, 그리고 전 여자친구 제인과 재회하게 되고, 그녀가 묠니르를 휘두르는 마이티 토르가 되어 나타나 모두를 놀라게 한다. 이제 팀 토르는 고르의 복수에 얽힌 미스터리를 밝히고 더 큰 전쟁을 막기 위한 전 우주적 스케일의 모험을 시작하는데...",
            "poster_path": "/un8ZDtx2SMwNwXRYy65aItnNjab.jpg",
            "genres": [
              14,
              28,
              35
            ]
          },
          "created_at": "2022-11-16T15:48:47.485650",
          "best_of_best": false,
          "user": [
              1
          ]
      },
      {
          "id": 3,
          "movie": {
            "title": "피노키오",
            "released_date": "2022-09-07",
            "popularity": 1033.698,
            "vote_count": 1063,
            "vote_avg": 6.7,
            "overview": "목수 ‘제페토’의 간절한 소원으로 태어난 나무 인형 ‘피노키오’는  진짜 사람이 되기 위해 자신의 양심이 되어줄 귀뚜라미 ‘지미니’와 함께  진실되고 용감한 마음을 가지기로 약속한다.  그러나 거리의 교활한 여우의 꾀임에 넘어간 피노키오는 서커스단에 들어가게 되고, 이기적인 어른들의 욕심으로 철장에 갇혀버리고 만다.  한편, 사라진 피노키오를 찾기 위해 길을 나선 ‘제페토’는 폭우 속에 목숨을 잃을 위기에 처하고 마는데…",
            "poster_path": "/aFVjf2zcFzoNgbDKDEHiIw2g1DR.jpg",
            "genres": [
              14,
              12,
              10751
            ]
          },
          "created_at": "2022-11-16T15:48:47.485650",
          "best_of_best": false,
          "user": [
              1
          ]
      },
    ],
  },
  getters: {
    // 로그인 여부 확인
    isLogin(state) {
      // return state.token ? true : false
      state
      return true
    }
  },
  mutations: {
    // auth
    SAVE_TOKEN(state, token) {
      state.token = token
      // 유저정보 불러오기
      this.$store.actions.getUser()
      // 저장한 영화가 없는 경우
      if (!state.best_movie) {
        router.push({ name: 'first-addMovie'})
      } else {
        router.push({ name: 'home'})
      }
    },

    // best_movie(인생영화), all_best_movies(명에의 전당) 저장
    GET_USER(state, data) {
      state.all_best_movies = data['best_movies']
      const idx = state.all_best_movies.findLastIndex((record) => {record.best_of_best === true})
      state.best_movie = state.all_best_movies[idx]
    }
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          email, password1, password2
        }
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err => console.log(err))
    },
    // 로그인
    login(context, payload) {
      const email = payload.email
      const password = payload.password

      // axios({
      //   method: 'post',
      //   url: `${API_URL}/accounts/login/`,
      //   data: {
      //     email, password
      //   }
      // })
      // .then(res => {
      //   context.commit('SAVE_TOKEN', res.data.key)
      // })
      // .catch(err => console.log(err))
      
      this.state.email = email
      this.state.password = password
      
    },
    // 유저 정보
    getUser(context) {
      console.log('here')
      axios({
        method: 'get',
        url: `${API_URL}/api/accounts/${context.state.user_pk}`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then(res => {
        console.log(res)
        context.commit('GET_USER', res.data)
      })
    },
  },
  modules: {
  }
})
