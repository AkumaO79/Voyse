dropContainer.ondragover = dropContainer.ondragenter = function (evt) {
    evt.preventDefault();
};
dropContainer.ondrop = function (evt) {
    fileInput.files = evt.dataTransfer.files;

    evt.preventDefault();
};