var buttonColours = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];
var id;
var userChosenColour;
var count = 0;
var i = 0;
var k = 0;
var j = 0;



$("h1").on("click", function(event) {
  if (k != 1) {
    nextSequence();
    $("body").removeClass("game-over");
    k = 1;
  }
});

$(document).on("keypress", function(event) {
  if (j != 1) {
    nextSequence();
    $("body").removeClass("game-over");
    j = 1;
  }
});

$(".btn").click(function(event) {
  userChosenColour = event.target.id; //or we can use var userChosenColour=$(".btn").attr("id");
  userClickedPattern.push(userChosenColour);
  var buttonClickSound = "sounds/" + userChosenColour + ".mp3";
  $("#" + userChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
  sound(buttonClickSound);
  console.log("the gamePattern is" + gamePattern);
  console.log("the userPattern is" + userClickedPattern);
  checkAnswer(userClickedPattern.length - 1);
});

function sound(sound) {
  var audio = new Audio(sound);
  audio.play();
}


function checkAnswer(currentlevel) {
  if (gamePattern[currentlevel] === userClickedPattern[currentlevel]) {
    console.log("success " + i + " out of " + gamePattern.length);

    if (userClickedPattern.length === gamePattern.length) {
      setTimeout(function() {
        nextSequence();
      }, 1000);
    }
  }
  else{
        gameOver();
      }
}

function gameOver() {
  console.log("fail");
  document.querySelector("h1").innerHTML="Game Over Chomu 😜, Click on the heading to Restart";
  var wrong = "sounds/wrong.mp3";
  sound(wrong);
  $("body").addClass("game-over");
  setTimeout(function() {
    $("body").addClass("game-over");
  }, 100);
  setTimeout(function() {
    $("body").removeClass("game-over");
  }, 200);
  setTimeout(function() {
    $("body").addClass("game-over");
  }, 300);
  setTimeout(function() {
    $("body").removeClass("game-over");
  }, 400);
  setTimeout(function() {
    $("body").addClass("game-over");
  }, 500);
  setTimeout(function() {
    $("body").removeClass("game-over");
  }, 600);
  setTimeout(function() {
    $("body").addClass("game-over");
  }, 700);
  j = 0;
  k=0
  count = 0;
  gamePattern = [];
  userClickedPattern = [];
}

function nextSequence()
{
  userClickedPattern = [];
  count++;
  $("h1").text("level " + count);
  var randomNumber = Math.floor(Math.random() * 4);
  var randomChosenColour = buttonColours[randomNumber];
  gamePattern.push(randomChosenColour);
  var id = "#" + randomChosenColour;
  $(id).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
  var music = "sounds/" + randomChosenColour + ".mp3";
  sound(music);
}
