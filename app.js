// import { connect } from "mqtt"  // import connect from mqtt
// const mqtt = require('mqtt')
// const client  = mqtt.connect('mqtt://test.mosquitto.org')

// client.on('connect', function () {
//   client.subscribe('presence', function (err) {
//     if (!err) {
//       client.publish('presence', 'Hello mqtt')
//     }
//   })
// })

// client.on('message', function (topic, message) {
//   // message is Buffer
//   console.log(message.toString())
//   client.end()
// })

// Create the PixiJS application
const app = new PIXI.Application({
    width: 800,
    height: 800,
    backgroundColor: 0x000000,
  });
  
  // Add the canvas to the HTML document
  document.body.appendChild(app.view);
  
  // Define the size of the grid
  const gridSize = 40;
  const squareSize = app.renderer.width / gridSize;
  
  // Function to generate a list of 500 colors from white to dark purple
  function generateColorList() {
    const colorList = [];
    const step = 500; // Number of steps in the gradient
  
    for (let i = 0; i < step; i++) {
      const gradientStep = i % step; // Calculate the step within the gradient
      const color = PIXI.utils.rgb2hex([1 - gradientStep / step, 0, 1 - gradientStep / step]);
      colorList.push(color);
    }
  
    return colorList;
  }
  
  // Function to randomly select a color from the color list
  function getRandomColor(colorList) {
    const randomIndex = Math.floor(Math.random() * colorList.length);
    return colorList[randomIndex];
  }
  
  // Function to create a square with a randomly selected color
  function createSquare(x, y, colorList) {
    const square = new PIXI.Graphics();
    square.beginFill(getRandomColor(colorList));
    square.drawRect(x * squareSize, y * squareSize, squareSize, squareSize);
    square.endFill();
    return square;
  }
  
  // Create the grid
  const grid = [];
  const colorList = generateColorList();
  for (let x = 0; x < gridSize; x++) {
    for (let y = 0; y < gridSize; y++) {
      const square = createSquare(x, y, colorList);
      app.stage.addChild(square);
      grid.push(square);
    }
  }
  
  // Function to rapidly change the color of each square using a randomly selected color
  function rapidlyChangeColor() {
    grid.forEach((square) => {
      square.tint = getRandomColor(colorList);
    });
  }
  
  // Call the rapidlyChangeColor function repeatedly every 100 milliseconds
  setInterval(rapidlyChangeColor, 10);
  