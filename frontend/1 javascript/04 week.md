---
marp: true
---

# [ITEC] JS Study

> 4 week

> strings, array

> ⓒ yoon sang seok all rights reserved.

---

# Contents

0. 챌린지 코드 리뷰
1. String
2. Array

---

# 0. 첼린지 코드 리뷰

---

# 1. String

- Template Literals
- includes method
- repeat method
- split method

---

## Template Literals

```js
const wrapper = document.querySelector(".wrap");

const addWelcome = () => {
  // const helloBox = document.createElement("div");
  // const h1 = document.createElement("h1");
  // h1.innerText = "hello";
  // helloBox.append(h1);
  // wrapper.append(helloBox);

  const helloBox = `
    <div class="hello">
      <h1 class="title">Hello</h1>
    </div>
  `;

  wrapper.innerHTML = helloBox;
};

addWelcome();
```

---

## includes method

```js
const isEmail = (email) => email.includes("@");

console.log(isEmail("amamov@amamov.com")); // true
```

---

## repeat method

```js
const CC_NUMBER = "6060";

const displayName = `${"*".repeat(10)}${CC_NUMBER}`;

console.log(displayName); // **********6060
```

---

## split method

```js
const data = "django@gmail.com";

// @ 기준으로 django와 gmail.com 분리하기

const result = data.split("@");
```

---

# 2. Array

---

## Array 생성자

- `Array()` : Array 객체를 생성한다.

## Array 정적 메서드

- `Array.from()`: array-like object나 iterable object을 얕게 복사해서 새로운 Array 객체를 만든다.
- `Array.of()` : 전달인자를 타입에 관계 없이 새로운 Array를 만든다.

## Array 속성 메서드

- `Array.prototype.length`

---

## Array 변경자 메서드

- `Array.prototype.pop()`
- `Array.prototype.push()`
- `Array.prototype.shift()`
- `Array.prototype.unshift()`
- `Array.prototype.reverse()`
- `Array.prototype.sort()`
- `Array.prototype.splice()` : 배열 **수정**, 제거
- `Array.prototype.fill()`

---

## Array 접근자 메서드 (새로운 객체를 반환)

- `Array.prototype.includes()` : `true`/`false` 반환
- `Array.prototype.slice()`
- `Array.prototype.join()`

---

## Array 순회 메서드

- `Array.prototype.find()`
- `Array.prototype.filter()`
- `Array.prototype.forEach()`
- `Array.prototype.map()`

---

## Array.from()

```js
const buttons = document.getElementsByClassName("btn");

console.log(buttons); // HTMLCollection Type 이므로 Array Type으로 바꿔주고 싶다.

Array.from(buttons).forEach((button) => console.log(button));
```

---

## Array.prototype.find()

[doc](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/find)

- 조건으로 만족하는 첫 번째 item을 반환한다.

```js
const myArray = [
  "amamov@gmail.com",
  "naver@gmail.com",
  "joy@naver.com",
  "hello@daum.net",
  "world@wow.com",
];

// 조건으로 만족하는 첫 번째 item을 반환한다.
const foundItem = myArray.find((item) => item.includes("@gmail.com"));

console.log(foundItem); // amamov@gmail.com
```

---

## Array.prototype.filter()

[doc](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

- 조건으로 만족하는 모든 item을 반환한다.

```js
const data = [
  "yss@gmail.com",
  "django@gmail.com",
  "react@kakao.com",
  "summer@amamov.con",
  "joy@naver.com",
  "hello@daum.net",
  "yyr@gmail.com",
  "world@wow.com",
];

// filter method를 사용하여 gmail을 사용하는 유저를 담은 배열을 뽑기
// [hint] filter, includes
// [출력] ['yss', 'django', 'yyr']
```

---

## Array.prototype.forEach()

[doc](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

- 배열을 순회하면서 각 요소에 대해 액션을 **수행한다.**

```js
const data = [
  "yss",
  "django",
  "react",
  "summer",
  "joy",
  "hello",
  "yyr",
  "world",
];

// forEach method를 사용하여 각각의 유저들을 출력하되, 뒤에 @gmail.com을 붙여서 출력하기
// [hint] forEach, +
// [출력] yss@gmail.com django@gmail.com ...
```

---

## Array.prototype.map()

[doc](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

- 배열을 순회하면서 각 요소에 대한 함수의 반환 값을 리턴한다.

```js
const myArray = [
  "yss@gmail.com",
  "django@gmail.com",
  "react@kakao.com",
  "summer@amamov.con",
  "joy@naver.com",
  "hello@daum.net",
  "yyr@gmail.com",
  "world@wow.com",
];

// map method를 사용하여 유저 이름을 뽑아내기
// [hint] map, split
// [출력] [ 'yss', 'django', 'react', 'summer', 'joy', 'hello', 'yyr', 'world' ]
```

---

# 👻

> ⓒ yoon sang seok all rights reserved.
