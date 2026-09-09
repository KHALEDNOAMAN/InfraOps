import React from 'react';

const colors: Record<string, string> = {
  active: 'bg-green-500/20 text-green-400 border-green-500/50',
  maintenance: 'bg-yellow-500/20 text-yellow-400 border-yellow-500/50',
  retired: 'bg-gray-500/20 text-gray-400 border-gray-500/50',
  alert: 'bg-red-500/20 text-red-400 border-red-500/50',
};

export default function StatusBadge({ status }: { status: string }) {
  const color = colors[status.toLowerCase()] || colors.active;
  return (
    <span className={`px-2 py-1 text-xs font-medium rounded-full border ${color} capitalize`}>
      {status}
    </span>
  );
}
