define(["window", "pixi"], function (window, PIXI) {
    "use strict";
    var renderer = PIXI.autoDetectRenderer(
        800,
        600,
        {
            backgroundColor: 0xffffff
        }
    );
    window.document.body.appendChild(renderer.view);

    // create the root of the scene graph
    var stage = new PIXI.Container();

    // create a new Sprite using the texture
    var airplane = new PIXI.Sprite(
        PIXI.Texture.fromImage("/airplane.png")
    );

    // center the sprite's anchor point
    airplane.anchor.x = 0.5;
    airplane.anchor.y = 0.5;

    // move the sprite to the center of the screen
    airplane.position.x = 200;
    airplane.position.y = 150;

    stage.addChild(airplane);
    // start animating
    function animate() {
        window.requestAnimationFrame(animate);

        // update(stage, time_elapsed);

        // just for fun, let's rotate mr rabbit a little
        airplane.rotation += 0.05;

        // render the container
        renderer.render(stage);
    }
    animate();
});
