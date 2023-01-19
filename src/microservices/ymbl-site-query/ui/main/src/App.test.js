import { render, screen } from '@testing-library/react';
import Standings from './routes/Standings';
import Schedule from './routes/Schedule';
import Stats from './routes/Stats';

// Standings Page Tests //
test('Navigation bar is rendered for standings page', () => {
  render(<Standings />);
  const navBar = screen.getByRole("navigation");
  expect(navBar).toBeInTheDocument();
});

test('Static info is rendered for standings page', () => {
  render(<Standings />);
  const linkElement = screen.getByText(/Regular Season Standings/i);
  expect(linkElement).toBeInTheDocument();
});


// Schedule Page Tests //
test('Navigation bar is rendered for schedule page', () => {
  render(<Schedule />);
  const navBar = screen.getByRole("navigation");
  expect(navBar).toBeInTheDocument();
});

test('Static info is rendered for schedule page', () => {
  render(<Schedule />);
  const linkElement = screen.getByText(/Regular Season Schedule/i);
  expect(linkElement).toBeInTheDocument();
});


// Stats Page Tests //
test('Navigation bar is rendered for stats page', () => {
  render(<Stats />);
  const navBar = screen.getByRole("navigation");
  expect(navBar).toBeInTheDocument();
});

test('Static info is rendered for schedule page', () => {
  render(<Stats />);
  const linkElement = screen.getByText(/Player Stats/i);
  expect(linkElement).toBeInTheDocument();
});