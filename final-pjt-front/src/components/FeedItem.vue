<template>
  <div>
    <hr>
    <h2>FeedItem</h2>
    {{feedItem.movie.title}}
    <br>
    {{feedItem.user.username}}
    <hr>

  </div>
</template>

<script>
export default {
  name: 'FeedItem',
  props: {
    feedItem: Object,
  }
  // *참고* 개별 feeditem은 다음과 같이 주어집니다. (프론트 작업 이후 지워주세요)
  // {
  //    "id": 6,
  //    "movie": {
  //        "id": 634649,
  //        "genres": [
  //            {
  //                "id": 12,
  //                "name": "모험"
  //            },
  //            {
  //                "id": 28,
  //                "name": "액션"
  //            },
  //            {
  //                "id": 878,
  //                "name": "SF"
  //            }
  //        ],
  //        "countries": [
  //            {
  //                "id": 2,
  //                "name": "미국"
  //            }
  //        ],
  //        "title": "스파이더맨: 노 웨이 홈",
  //        "original_title": "Spider-Man: No Way Home",
  //        "released_date": "2021-12-15",
  //        "popularity": 812.372,
  //        "vote_count": 15857,
  //        "vote_avg": 8.0,
  //        "overview": "미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 사상 최악의 위기를 맞게 되는데…",
  //        "poster_path": "/voddFVdjUoAtfoZZp2RUmuZILDI.jpg",
  //        "backdrop_path": "/14QbnygCuTO0vl7CAFmPf1fgZfV.jpg",
  //        "trailer_path": "WgU7P6o-GkM",
  //        "recommended": [
  //            335787,
  //            338953,
  //            414906,
  //            425909,
  //            429617,
  //            453395,
  //            476669,
  //            507086,
  //            508947,
  //            524434,
  //            526896,
  //            566525,
  //            568124,
  //            580489,
  //            616037,
  //            624860,
  //            646380,
  //            675353,
  //            696806
  //        ]
  //    },
  //    "user": {
  //        "id": 2,
  //        "username": "test2",
  //        "avatar": "/images/default_avatar_2.svg"
  //    },
  //    "created_at": "2022-11-22T14:15:16.099660",
  //    "best_of_best": true
  // },
}
</script>

<style>

</style>