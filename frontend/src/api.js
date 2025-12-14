export const verifyDocument = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:5000/verify-document", {
    method: "POST",
    body: formData
  });

  return response.json();
};
