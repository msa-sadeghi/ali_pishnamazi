let basket = [];
const products = [
  {
    id: 1,
    title: "laptop Hp Omni book Ultra 14",
    price: 400,
    imgUrl: "https://hp.widen.net/content/ihsigjyy8p/webp/ihsigjyy8p.png",
  },
  {
    id: 2,
    title: "laptop Hp # 2",
    price: 300,
    imgUrl: "https://hp.widen.net/content/ihsigjyy8p/webp/ihsigjyy8p.png",
  },
  {
    id: 3,
    title: "laptop Hp # 3",
    price: 250,
    imgUrl: "https://hp.widen.net/content/ihsigjyy8p/webp/ihsigjyy8p.png",
  },
  {
    id: 4,
    title: "laptop Hp # 4",
    price: 200,
    imgUrl: "https://hp.widen.net/content/ihsigjyy8p/webp/ihsigjyy8p.png",
  },
];

const rootElemet = document.getElementById("root");
const addItem = (pid) => {
  const product = products.find((p) => p.id === pid);
  const searchResultIndex = basket.findIndex((p) => p.productId === product.id);
  console.log(searchResultIndex);
  if (searchResultIndex === -1) {
    const newItem = {
      id: Date.now(),
      productId: pid,
      title: product.title,
      price: product.price,
      count: 1,
    };
    basket.push(newItem);
  } else {
    basket[searchResultIndex].count++;
  }
  updateHeader();
};
window.onload = () => {
  const productsElements = products.map(
    (p) => `<div class="card">
            <img src=${p.imgUrl}/>
            <h3>${p.title}</h3>
            <div class="price">
              <span>price: </span>
              <span>${p.price}</span>
            </div>
            <div class="buttons">
              <button onclick=addItem(${p.id})>Add</button>
              <button></button>

            </div>
          </div>`,
  );

  productsElements.forEach((pE) => {
    console.log(typeof pE);
    rootElemet.innerHTML += pE;
  });
};

const totalCountContainerElement = document.createElement("div");
const basketElement = document.createElement("div");
basketElement.setAttribute("id", "basketElements");
totalCountContainerElement.append(basketElement);
const totalCountTitleElement = document.createElement("span");
const totalCountElement = document.createElement("span");
totalCountTitleElement.setAttribute("id", "count");
totalCountTitleElement.innerText = "total Count:";
totalCountContainerElement.append(totalCountTitleElement);
totalCountContainerElement.append(totalCountElement);
rootElemet.append(totalCountContainerElement);
function updateHeader() {
  const basketElements = document.getElementById("basketElements");
  const items = basket
    .map(
      (item) => `<div>
    <h3>${item.title}</h3>
    <p>count : ${item.count}</p>
    <p>${item.price}</p>
    </div>`,
    )
    .join("");

  basketElements.innerHTML = items;
  const countElemet = document.getElementById("count");
  let totalCount = 0;
  basket.forEach((item) => {
    totalCount += item.count;
  });
  countElemet.innerHTML = `total Count : ${totalCount}`;
}
updateHeader();
