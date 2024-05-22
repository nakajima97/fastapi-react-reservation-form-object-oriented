import camelcaseKeys from "camelcase-keys";

const fetchData = async (url: string) => {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error("Failed to fetch data");
  }

  const data = await response.json();
  return camelcaseKeys(data.reservations);
}

export {
  fetchData
}