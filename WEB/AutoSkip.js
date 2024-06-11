// Simple script runs on "some page" and plays unskippable audios one by one and moves to the next screen. For experimental purposes only, dunno if this can be used in real life...
const func = () => {
  let button = document
    .querySelector(".directional__nav__button__container--next")
    .querySelector(".ember-view");
  if (button.classList.contains("disabled")) {
    // Click on audio button
    if (
      document.querySelector(".audio-player__play-button") == null ||
      document.querySelector(".audio-player__play-button") == undefined
    ) {
      alert("No audio button found");
      // End here
    } else {
      document.querySelector(".audio-player__play-button").click();
      // Wait 5 seconds
      setTimeout(() => {
        try {
          let duration = document
            .querySelector(".position")
            .innerText.split("/")[1];
          // Convert to seconds
          let seconds = parseInt(duration.split(":")[0]) * 60;
          seconds += parseInt(duration.split(":")[1]);
          // SetTimeOut in seconds (Function runs itself again)
          setTimeout(func, seconds * 1000);
        } catch (e) {
          ``;
          alert("No duration found");
        }
      }, 5000);
    }
  } else {
    let actualBtn = document
      .querySelector(".directional__nav__button__container--next")
      .querySelector(".directional__nav__button--right");
    actualBtn.click();
    // SetTimeOut in 5 seconds (Function runs itself again)
    setTimeout(func, 5000);
  }
  // To start
  setTimeout(func, 1000);
};
// ..It can :)
