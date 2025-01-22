document.getElementById('back-to-top').addEventListener('click', function(e) {
    e.preventDefault(); // Evita el comportamiento por defecto del enlace
    smoothScrollTo(0, 0);
  });
  
  function smoothScrollTo(endX, endY, duration = 500) {
    const startX = window.scrollX || window.pageXOffset;
    const startY = window.scrollY || window.pageYOffset;
    const distanceX = endX - startX;
    const distanceY = endY - startY;
    const startTime = performance.now();
  
    function step(currentTime) {
      const progress = Math.min((currentTime - startTime) / duration, 1);
      const ease = progress < 0.5 
        ? 4 * progress * progress * progress 
        : 1 - Math.pow(-2 * progress + 2, 3) / 2;
  
      window.scrollTo(
        startX + distanceX * ease,
        startY + distanceY * ease
      );
  
      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }
  
    requestAnimationFrame(step);
  }
  