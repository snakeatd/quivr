interface UfroLogoProps {
  size: number;
  color?: "white" | "black" | "primary" | "accent";
}

export const UfroLogo = ({
  size,
  color = "white",
}: UfroLogoProps): JSX.Element => {
  const colorMap: Record<string, string> = {
    white: "#ffffff",
    black: "#1A2E1A",
    primary: "#006633",
    accent: "#C8963C",
  };

  const fill = colorMap[color] ?? colorMap.white;

  return (
    <svg
      width={size * 2.5}
      height={size}
      viewBox="0 0 250 100"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      aria-label="UFRO Logo"
    >
      {/* Green bar on top */}
      <rect x="0" y="0" width="250" height="12" rx="4" fill={fill} opacity="0.8" />

      {/* UFRO text */}
      <text
        x="125"
        y="72"
        textAnchor="middle"
        fontFamily="'Arial', 'Helvetica', sans-serif"
        fontWeight="800"
        fontSize="52"
        letterSpacing="6"
        fill={fill}
      >
        UFRO
      </text>

      {/* Subtitle */}
      <text
        x="125"
        y="92"
        textAnchor="middle"
        fontFamily="'Arial', 'Helvetica', sans-serif"
        fontWeight="400"
        fontSize="11"
        letterSpacing="2"
        fill={fill}
        opacity="0.75"
      >
        Universidad de La Frontera
      </text>
    </svg>
  );
};
