<!DOCTYPE html>
<html>
<head>
    <title>Moving Tulip Flower</title>
    <style>
        /* Style for the tulip image */
        #tulip {
            position: absolute;
            top: 0;
            left: 0;
            width: 100px; /* Adjust the size of the tulip */
            height: 100px; /* Adjust the size of the tulip */
            transition: top 1s, left 1s; /* Animation duration */
        }
    </style>
</head>
<body>
    <img id="tulip" src="tulip.png" alt="Tulip">

    <script>
        // Get the tulip element
        var tulip = document.getElementById("tulip");

        // Set the initial position of the tulip
        var tulipX = 0;
        var tulipY = 0;

        // Movement speed
        var speed = 5;

        // Function to update the tulip position
        function updateTulipPosition() {
            // Update tulip position
            tulipX += speed;
            tulipY += speed;

            // If tulip goes off the screen, reset its position
            if (tulipX > window.innerWidth || tulipY > window.innerHeight) {
                tulipX = 0;
                tulipY = 0;
            }

            // Set the new position of the tulip
            tulip.style.left = tulipX + "px";
            tulip.style.top = tulipY + "px";

            // Call the function recursively to create animation
            requestAnimationFrame(updateTulipPosition);
        }

        // Start the animation
        updateTulipPosition();
    </script>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>Moving Tulip Flower</title>
    <style>
        /* Style for the tulip image */
        #tulip {
            position: absolute;
            top: 0;
            left: 0;
            width: 100px; /* Adjust the size of the tulip */
            height: 100px; /* Adjust the size of the tulip */
            transition: top 1s, left 1s; /* Animation duration */
        }
    </style>
</head>
<body>
    <img id="tulip" src="tulip.png" alt="Tulip">

    <script>
        // Get the tulip element
        var tulip = document.getElementById("tulip");

        // Set the initial position of the tulip
        var tulipX = 0;
        var tulipY = 0;

        // Movement speed
        var speed = 5;

        // Function to update the tulip position
        function updateTulipPosition() {
            // Update tulip position
            tulipX += speed;
            tulipY += speed;

            // If tulip goes off the screen, reset its position
            if (tulipX > window.innerWidth || tulipY > window.innerHeight) {
                tulipX = 0;
                tulipY = 0;
            }

            // Set the new position of the tulip
            tulip.style.left = tulipX + "px";
            tulip.style.top = tulipY + "px";

            // Call the function recursively to create animation
            requestAnimationFrame(updateTulipPosition);
        }

        // Start the animation
        updateTulipPosition();
    </script>
</body>
</html>

