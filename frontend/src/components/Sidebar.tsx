import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Building2, Server, RefreshCw, BarChart3, GitPullRequest, Key } from 'lucide-react';

const navItems = [
  { icon: LayoutDashboard, label: 'Dashboard', path: '/dashboard' },
  { icon: Building2, label: 'Data Centers', path: '/datacenters' },
  { icon: Server, label: 'Assets', path: '/assets' },
  { icon: RefreshCw, label: 'Lifecycle', path: '/lifecycle' },
  { icon: BarChart3, label: 'Capacity', path: '/capacity' },
  { icon: GitPullRequest, label: 'Changes', path: '/changes' },
  { icon: Key, label: 'Licenses', path: '/licenses' },
];

export default function Sidebar() {
  return (
    <div className="w-64 bg-gray-900 h-full border-r border-gray-800 flex flex-col">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-cyan-400">InfraOps</h1>
      </div>
      <nav className="flex-1 px-4 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive ? 'bg-gray-800 text-cyan-400' : 'text-gray-400 hover:bg-gray-800 hover:text-gray-100'
                }`
              }
            >
              <Icon size={20} />
              <span>{item.label}</span>
            </NavLink>
          );
        })}
      </nav>
      <div className="p-4 border-t border-gray-800 text-sm text-gray-500">
        v1.0.0
      </div>
    </div>
  );
}
