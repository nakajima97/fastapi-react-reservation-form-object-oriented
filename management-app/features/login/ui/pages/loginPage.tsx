"use client";

import { Box, TextField, Typography, Button } from "@mui/material";

type Props = {
  handleSubmit: () => void;
};

const loginPage = ({ handleSubmit }: Props) => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 2,
        width: "100%",
        maxWidth: "500px",
        margin: "auto",
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "10px",
      }}
    >
      <Typography variant="h4">ログイン</Typography>
      <TextField
        required
        id="email"
        label="Email Address"
        name="email"
        autoComplete="email"
        autoFocus
      />
      <TextField
        required
        id="password"
        label="Password"
        name="password"
        autoComplete="password"
        type="password"
        autoFocus
      />
      <Button
        type="submit"
        variant="contained"
        onClick={handleSubmit}
        fullWidth
      >
        ログイン
      </Button>
    </Box>
  );
};

export default loginPage;
